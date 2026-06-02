# Your First Topology

Before designing assignments, let's walk through the full lifecycle of a Containerlab topology: **write → deploy → interact → destroy**. This chapter uses a simple three-node topology that you can hand to students as a warmup exercise.

---

## The Topology: A Linear Network

We will create three Linux containers in a line:

```
[client] ── eth1:eth1 ── [router] ── eth2:eth2 ── [server]
```

- `client` and `server` represent end hosts
- `router` is a Linux container acting as a packet forwarder
- Each node runs Alpine Linux (tiny, fast, no licensing required)

---

## Step 1: Write the Topology File

Create a file named `linear.yaml`:

```yaml
name: linear

topology:
  nodes:
    client:
      kind: linux
      image: alpine:latest
      exec:
        - ip addr add 10.0.1.1/24 dev eth1
        - ip route add 10.0.2.0/24 via 10.0.1.2

    router:
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
    - endpoints: ["client:eth1", "router:eth1"]
    - endpoints: ["router:eth2", "server:eth2"]
```

### What's Happening Here?

| Key | Meaning |
|---|---|
| `name` | Prefix applied to all container names (e.g. `clab-linear-client`) |
| `kind: linux` | Plain Linux container — no vendor NOS needed |
| `image` | Docker image to use for this node |
| `exec` | Shell commands run inside the container immediately after startup |
| `endpoints` | `"node:interface"` pairs — Containerlab creates a veth link between them |

The `exec` block is how we configure IP addresses and routes at deploy time. This is equivalent to a startup config on a real router.

---

## Step 2: Deploy

```bash
sudo clab deploy -t linear.yaml
```

You will see Containerlab pull the Alpine image (first time only), create the containers, wire up the links, and run the exec commands. Typical output:

```
INFO[0000] Containerlab v0.75.0 started
INFO[0000] Parsing & checking topology file: linear.yaml
INFO[0001] Creating lab directory: /root/clab-linear
INFO[0002] Creating container: client
INFO[0002] Creating container: router
INFO[0002] Creating container: server
INFO[0003] Creating link: client:eth1 <--> router:eth1
INFO[0003] Creating link: router:eth2 <--> server:eth2
INFO[0005] 3 nodes, 2 links deployed in 5 seconds
```

---

## Step 3: Inspect the Running Topology

```bash
sudo clab inspect -t linear.yaml
```

Output:

```
+---+---------------------+--------------+-------------+---------+
| # | Name                | Container ID | Image       | State   |
+---+---------------------+--------------+-------------+---------+
| 1 | clab-linear-client  | a1b2c3d4e5f6 | alpine:latest | running |
| 2 | clab-linear-router  | b2c3d4e5f6a1 | alpine:latest | running |
| 3 | clab-linear-server  | c3d4e5f6a1b2 | alpine:latest | running |
+---+---------------------+--------------+-------------+---------+
```

---

## Step 4: Interact with Nodes

You can open a shell in any node using `docker exec`:

```bash
sudo docker exec -it clab-linear-client sh
```

Or run a single command without entering an interactive shell:

```bash
sudo docker exec clab-linear-client ping -c 4 10.0.2.1
```

Expected output:

```
PING 10.0.2.1 (10.0.2.1): 56 data bytes
64 bytes from 10.0.2.1: seq=0 ttl=63 time=0.312 ms
64 bytes from 10.0.2.1: seq=1 ttl=63 time=0.287 ms
```

Notice `ttl=63` — the packet crossed the router, which decremented the TTL by 1 from the default of 64. This is real routing behaviour.

---

## Step 5: Capture Traffic

Containerlab nodes use real Linux network interfaces, so `tcpdump` works natively:

```bash
# On the router, capture all traffic on eth1
sudo docker exec clab-linear-router tcpdump -i eth1 -n
```

While that is running, send pings from another terminal:

```bash
sudo docker exec clab-linear-client ping -c 3 10.0.2.1
```

You will see the ICMP packets appear in the tcpdump output in real time.

---

## Step 6: Destroy

```bash
sudo clab destroy -t linear.yaml
```

All containers, interfaces, and routes are removed. The system is back to its original state.

---

## Summary: The Containerlab Workflow

```{mermaid}
graph LR
    A[Write topology YAML] --> B[clab deploy]
    B --> C[Containers running\nLinks wired\nexec commands run]
    C --> D[Students interact\ndocker exec / SSH]
    D --> E[clab destroy]
    E --> A
```

This loop — write, deploy, experiment, destroy — is the core workflow for every assignment in this guide. The next three chapters apply it to specific networking topics.
