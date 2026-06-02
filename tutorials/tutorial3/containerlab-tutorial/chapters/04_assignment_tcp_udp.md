# Assignment: TCP-like Reliability over UDP

## Learning Objectives

By the end of this assignment, students will be able to:

- Explain why UDP alone does not guarantee reliable delivery
- Implement stop-and-wait or sliding window ARQ in application code
- Use Containerlab to create a network environment with controlled packet loss
- Measure throughput and reliability of their implementation under adverse conditions

---

## Faculty Overview

This is a classic transport-layer programming assignment, but Containerlab adds something that a pure coding exercise cannot: **a real network with real packet loss**. Rather than simulating loss inside the program, students experience loss imposed by the network itself — which is much closer to real-world conditions and forces them to think about timeouts, retransmissions, and sequence numbers at the right level of abstraction.

The topology is intentionally simple: one client and one server connected by a single link. The complexity comes from the link conditions applied with Linux Traffic Control (`tc`).

---

## Topology

```
[client] ── eth1 ─────────── eth1 ── [server]
              (lossy / delayed link)
```

### Topology File: `udp-reliability.yaml`

```yaml
name: udp-reliability

topology:
  nodes:
    client:
      kind: linux
      image: python:3.11-alpine
      exec:
        - ip addr add 10.0.0.1/24 dev eth1

    server:
      kind: linux
      image: python:3.11-alpine
      exec:
        - ip addr add 10.0.0.2/24 dev eth1

  links:
    - endpoints: ["client:eth1", "server:eth1"]
```

We use `python:3.11-alpine` so students can write and run Python directly inside the containers without installing anything.

---

## Setting Up Link Impairments

After deploying the topology, apply network impairments using Linux `tc` (traffic control). This is run **inside** the client container:

```bash
sudo docker exec clab-udp-reliability-client sh -c \
  "tc qdisc add dev eth1 root netem loss 5% delay 50ms"
```

This command:

- `netem` — the Linux network emulator kernel module
- `loss 5%` — drops 5% of outgoing packets randomly
- `delay 50ms` — adds 50ms of latency to every packet

To remove the impairment:

```bash
sudo docker exec clab-udp-reliability-client sh -c \
  "tc qdisc del dev eth1 root"
```

---

## Suggested Assignment Structure

### Part 1 — Baseline (Week 1)

Ask students to write a **simple UDP sender and receiver** with no reliability mechanism:

```python
# sender.py (runs on client)
import socket, time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for i in range(100):
    sock.sendto(f"packet {i}".encode(), ("10.0.0.2", 5000))
    time.sleep(0.01)
print("Done sending 100 packets")
```

```python
# receiver.py (runs on server)
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 5000))
received = 0
while True:
    data, addr = sock.recvfrom(1024)
    received += 1
    print(f"Received: {data.decode()} | Total: {received}")
```

**Discussion question:** With 5% loss applied, approximately how many of the 100 packets arrive? Is this consistent? Why or why not?

---

### Part 2 — Stop-and-Wait ARQ (Week 2)

Students implement a **stop-and-wait** protocol:

- Sender sends one packet and waits for an ACK
- If no ACK arrives within a timeout, the sender retransmits
- Receiver sends an ACK for every packet it receives
- Both sides use sequence numbers to detect duplicates

**Packet format (suggested):**

```
| seq_num (4 bytes) | flags (1 byte) | payload (variable) |
```

Where `flags`: `0x01` = DATA, `0x02` = ACK.

**Deliverables:**
- Working sender and receiver implementing stop-and-wait
- Experiment: measure throughput (bytes/second) with 0%, 5%, 10%, 20% loss
- Plot: throughput vs. loss rate
- Short write-up explaining the observed relationship

---

### Part 3 — Sliding Window (Week 3, Advanced)

Students extend their implementation to a **sliding window** protocol with window size `W`:

- Sender can have up to `W` unacknowledged packets in flight
- Receiver sends cumulative ACKs
- Implement Go-Back-N or Selective Repeat (student's choice)

**Deliverables:**
- Working sliding window implementation
- Experiment: throughput vs. window size (W = 1, 4, 8, 16) at fixed 5% loss and 50ms delay
- Comparison with stop-and-wait results from Part 2
- Explanation: at what window size does performance stop improving and why?

---

## Useful Commands for Students

```bash
# Enter the client container
sudo docker exec -it clab-udp-reliability-client sh

# Copy a Python file into the container
sudo docker cp sender.py clab-udp-reliability-client:/sender.py

# Run the receiver in the background on the server
sudo docker exec -d clab-udp-reliability-server python3 /receiver.py

# Apply loss and delay
sudo docker exec clab-udp-reliability-client sh -c \
  "tc qdisc add dev eth1 root netem loss 10% delay 50ms"

# Verify current tc settings
sudo docker exec clab-udp-reliability-client tc qdisc show dev eth1

# Capture UDP traffic on the server to verify packets are arriving
sudo docker exec clab-udp-reliability-server \
  tcpdump -i eth1 udp port 5000 -n
```

---

## Faculty Notes

**Grading tips:**
- The topology file is the same for all students — what varies is their implementation code.
- Ask students to include a `README.md` describing how to run their code; this doubles as a test of their ability to write reproducible experiments.
- For Part 3, the most common mistake is students using the wrong window size unit (bytes vs. packets). Clarifying this in the assignment brief saves a lot of confusion.

**Common issues:**
- Students often forget that `tc` rules are lost when the container is destroyed and re-deployed. Remind them to re-apply `tc` after every `clab deploy`.
- Students on shared servers may accidentally exec into each other's containers if container names are the same. Enforce unique topology `name:` values per student (e.g. `name: udp-<student-id>`).

**Extension ideas:**
- Add a third node (middlebox) between client and server, and apply impairments there instead, making the path asymmetric.
- Ask students to implement a congestion window and observe how it interacts with the loss-based retransmission logic.
