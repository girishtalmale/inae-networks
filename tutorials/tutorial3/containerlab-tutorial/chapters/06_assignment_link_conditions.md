# Assignment: Dynamic Link Conditions

## Learning Objectives

By the end of this assignment, students will be able to:

- Apply and remove network impairments (delay, loss, bandwidth limits, jitter) using Linux `tc netem`
- Measure and explain the effect of each impairment type on application-layer behaviour
- Predict how TCP and UDP behave differently under the same network conditions
- Design a simple experiment, collect data, and draw conclusions

---

## Faculty Overview

This assignment teaches students how network conditions affect real applications. Rather than working from theoretical models, students use Linux Traffic Control (`tc`) to impose impairments on a live network and observe the effects with tools like `iperf3`, `ping`, and `tcpdump`.

The same topology from Chapter 3 (linear three-node network) is reused here, keeping the infrastructure simple so students focus on measurement rather than configuration.

---

## Topology

We use the same linear topology from Chapter 3, with one addition: a **middlebox** node where all impairments are applied. This cleanly separates "impairment logic" from "end-host logic".

```
[client] ── eth1:eth1 ── [middlebox] ── eth2:eth2 ── [server]
                          (tc rules here)
```

### Topology File: `link-conditions.yaml`

```yaml
name: linklab

topology:
  nodes:
    client:
      kind: linux
      image: alpine:latest
      exec:
        - ip addr add 10.0.1.1/24 dev eth1
        - ip route add 10.0.2.0/24 via 10.0.1.2

    middlebox:
      kind: linux
      image: alpine:latest
      exec:
        - sysctl -w net.ipv4.ip_forward=1
        - ip addr add 10.0.1.2/24 dev eth1
        - ip addr add 10.0.2.2/24 dev eth2

    server:
      kind: linux
      image: alpine:latest
      exec:
        - ip addr add 10.0.2.1/24 dev eth2
        - ip route add 10.0.1.0/24 via 10.0.2.2

  links:
    - endpoints: ["client:eth1", "middlebox:eth1"]
    - endpoints: ["middlebox:eth2", "server:eth2"]
```

---

## Linux `tc netem` Reference

All impairments are applied to the **middlebox's outgoing interface** (`eth2`), affecting traffic flowing toward the server.

### Add impairments

```bash
# Latency only — add 100ms delay
sudo docker exec clab-linklab-middlebox \
  tc qdisc add dev eth2 root netem delay 100ms

# Latency + jitter — 100ms ± 20ms
sudo docker exec clab-linklab-middlebox \
  tc qdisc add dev eth2 root netem delay 100ms 20ms

# Packet loss — 10% random loss
sudo docker exec clab-linklab-middlebox \
  tc qdisc add dev eth2 root netem loss 10%

# Bandwidth limit — cap at 1 Mbit/s (using tbf, not netem)
sudo docker exec clab-linklab-middlebox \
  tc qdisc add dev eth2 root tbf rate 1mbit burst 32kbit latency 400ms

# Combined — 50ms delay + 5% loss
sudo docker exec clab-linklab-middlebox \
  tc qdisc add dev eth2 root netem delay 50ms loss 5%

# Packet reordering — 25% of packets reordered by up to 10ms
sudo docker exec clab-linklab-middlebox \
  tc qdisc add dev eth2 root netem delay 10ms reorder 25% 50%
```

### Modify existing rules

```bash
# Change from 5% to 15% loss (use 'change' not 'add')
sudo docker exec clab-linklab-middlebox \
  tc qdisc change dev eth2 root netem loss 15%
```

### Remove all impairments

```bash
sudo docker exec clab-linklab-middlebox \
  tc qdisc del dev eth2 root
```

### Inspect current rules

```bash
sudo docker exec clab-linklab-middlebox \
  tc qdisc show dev eth2
```

---

## Measurement Tools

Install these inside containers as needed:

```bash
# iperf3 (bandwidth and latency measurement)
sudo docker exec clab-linklab-server apk add --no-cache iperf3
sudo docker exec clab-linklab-client apk add --no-cache iperf3

# Start iperf3 server
sudo docker exec -d clab-linklab-server iperf3 -s

# Run TCP throughput test from client
sudo docker exec clab-linklab-client iperf3 -c 10.0.2.1 -t 10

# Run UDP throughput test (with bandwidth target)
sudo docker exec clab-linklab-client iperf3 -c 10.0.2.1 -u -b 10M -t 10
```

---

## Suggested Experiments

Provide students with a structured experiment table to fill in:

### Experiment 1: Latency vs. TCP Throughput

| Delay (ms) | TCP Throughput (Mbps) | RTT (ms) observed by ping |
|---|---|---|
| 0 | | |
| 10 | | |
| 50 | | |
| 100 | | |
| 200 | | |

**Instructions:**
1. For each delay value, apply the tc rule, run `iperf3` for TCP (10 seconds), record throughput.
2. Simultaneously record the RTT using `ping -c 20`.
3. Remove the tc rule before moving to the next row.

**Discussion question:** As latency increases, what happens to throughput? Can you explain this using the concept of the TCP congestion window and the bandwidth-delay product?

---

### Experiment 2: Packet Loss vs. TCP and UDP

| Loss (%) | TCP Throughput (Mbps) | UDP Throughput (Mbps) | UDP Packet Loss (%) |
|---|---|---|---|
| 0 | | | |
| 1 | | | |
| 5 | | | |
| 10 | | | |
| 20 | | | |

**Instructions:**
1. Apply loss, run TCP iperf3, record throughput.
2. Apply the same loss, run UDP iperf3 at a fixed send rate (e.g. `-b 10M`), record reported throughput and loss.

**Discussion question:** How do TCP and UDP respond differently to packet loss? Which is more suitable for a video streaming application? A file transfer?

---

### Experiment 3: Bandwidth Cap

Apply a bandwidth limit on the middlebox and measure how different applications are affected:

```bash
# Cap at 512 kbit/s
sudo docker exec clab-linklab-middlebox \
  tc qdisc add dev eth2 root tbf rate 512kbit burst 32kbit latency 400ms
```

**Tasks:**
- Run `iperf3` and observe whether the throughput matches the configured cap.
- Start a `curl` download (or `wget`) of a large file from the server and observe transfer speed.
- Discuss: what happens when multiple flows share the same bottleneck link?

---

## Deliverables

Students submit:

1. Completed experiment tables (as a Markdown or CSV file)
2. Plots: throughput vs. latency and throughput vs. loss (one plot each, TCP and UDP overlaid where applicable)
3. Short write-up (600–900 words) addressing the discussion questions

---

## Faculty Notes

**Grading tips:**
- Results should show a clear trend (throughput degrades with loss/delay). If a student's numbers are flat or chaotic, they likely forgot to clear `tc` rules between experiments.
- The UDP vs. TCP comparison is often the most insightful part. Strong responses will mention TCP's retransmission and flow control mechanisms, while weaker ones will just describe the numbers without explanation.

**Common issues:**
- `tc qdisc add` fails with "File exists" if a rule is already set. Students must use `tc qdisc del` first.
- Bandwidth tests with `iperf3 -u` require setting a target bitrate with `-b`; without it, UDP defaults to 1 Mbit/s which may not reveal interesting behaviour.
- Some Alpine images lack `iperf3` by default — remind students to install it with `apk add --no-cache iperf3` inside the container.

**Extension ideas:**
- Add a **variable loss** model (`netem loss random 5% 25%` for bursty loss) and ask students to compare uniform vs. bursty loss on TCP performance.
- Introduce **asymmetric impairment**: apply delay in one direction only and observe its effect on TCP acknowledgement timing.
- Combine with the UDP reliability assignment: ask students to test their own ARQ implementation under these conditions.
