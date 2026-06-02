# Assignment: Network Topology Design

## Learning Objectives

By the end of this assignment, students will be able to:

- Design multi-subnet IP network topologies and justify routing decisions
- Translate a written network specification into a working Containerlab topology file
- Verify connectivity and routing paths using `ping`, `traceroute`, and `ip route`
- Reason about trade-offs in topology design (redundancy, cost, convergence)

---

## Faculty Overview

In this assignment, students design and implement a network topology from a set of requirements — much like a junior network engineer receiving a brief from a client. The deliverable is a **Containerlab topology YAML file** plus a short design document. Because the topology is declarative code, you can deploy it in seconds to verify it actually works.

This assignment scales well: you can give the same scenario to all students and evaluate whether their topologies meet the requirements, or give different scenarios to different groups to prevent copying.

---

## Scenario: A Small Campus Network

Present students with the following brief:

> **Acme University** needs a network connecting three buildings: the **Library**, the **Engineering Building**, and the **Administration Building**. Each building has its own subnet. All buildings must be able to reach each other. The Engineering Building also has a dedicated **Lab Subnet** for student experiments, which must be reachable from all other buildings but isolated at Layer 3 from the Administration subnet (i.e. the Lab cannot reach Admin directly — all traffic must pass through Engineering).

Students must design a topology that satisfies these requirements using Linux containers as routers and hosts.

---

## Reference Topology (One Valid Solution)

There is no single correct answer. Here is one valid design faculty can use as a reference:

```
[lib-host]──[lib-router]──┐
                           ├──[core-router]──[eng-router]──[eng-host]
[adm-host]──[adm-router]──┘                      │
                                              [lab-host]
```

### Subnets

| Segment | Subnet |
|---|---|
| Library LAN | 10.1.0.0/24 |
| Admin LAN | 10.2.0.0/24 |
| Library ↔ Core | 10.10.1.0/30 |
| Admin ↔ Core | 10.10.2.0/30 |
| Core ↔ Engineering | 10.10.3.0/30 |
| Engineering LAN | 10.3.0.0/24 |
| Lab LAN | 10.4.0.0/24 |

---

## Reference Topology File

```yaml
name: campus

topology:
  nodes:
    # Hosts
    lib-host:
      kind: linux
      image: alpine:latest
      exec:
        - ip addr add 10.1.0.10/24 dev eth1
        - ip route add default via 10.1.0.1

    adm-host:
      kind: linux
      image: alpine:latest
      exec:
        - ip addr add 10.2.0.10/24 dev eth1
        - ip route add default via 10.2.0.1

    eng-host:
      kind: linux
      image: alpine:latest
      exec:
        - ip addr add 10.3.0.10/24 dev eth1
        - ip route add default via 10.3.0.1

    lab-host:
      kind: linux
      image: alpine:latest
      exec:
        - ip addr add 10.4.0.10/24 dev eth1
        - ip route add default via 10.4.0.1

    # Routers
    lib-router:
      kind: linux
      image: alpine:latest
      exec:
        - sysctl -w net.ipv4.ip_forward=1
        - ip addr add 10.1.0.1/24 dev eth1
        - ip addr add 10.10.1.1/30 dev eth2
        - ip route add default via 10.10.1.2

    adm-router:
      kind: linux
      image: alpine:latest
      exec:
        - sysctl -w net.ipv4.ip_forward=1
        - ip addr add 10.2.0.1/24 dev eth1
        - ip addr add 10.10.2.1/30 dev eth2
        - ip route add default via 10.10.2.2

    core-router:
      kind: linux
      image: alpine:latest
      exec:
        - sysctl -w net.ipv4.ip_forward=1
        - ip addr add 10.10.1.2/30 dev eth1
        - ip addr add 10.10.2.2/30 dev eth2
        - ip addr add 10.10.3.1/30 dev eth3
        - ip route add 10.1.0.0/24 via 10.10.1.1
        - ip route add 10.2.0.0/24 via 10.10.2.1
        - ip route add 10.3.0.0/24 via 10.10.3.2
        - ip route add 10.4.0.0/24 via 10.10.3.2

    eng-router:
      kind: linux
      image: alpine:latest
      exec:
        - sysctl -w net.ipv4.ip_forward=1
        - ip addr add 10.10.3.2/30 dev eth1
        - ip addr add 10.3.0.1/24 dev eth2
        - ip addr add 10.4.0.1/24 dev eth3
        - ip route add default via 10.10.3.1
        # Lab cannot reach Admin directly — route blocked by omission
        # (no direct route from lab subnet to 10.2.0.0/24 at this router)

  links:
    - endpoints: ["lib-host:eth1",  "lib-router:eth1"]
    - endpoints: ["lib-router:eth2", "core-router:eth1"]
    - endpoints: ["adm-host:eth1",  "adm-router:eth1"]
    - endpoints: ["adm-router:eth2", "core-router:eth2"]
    - endpoints: ["core-router:eth3", "eng-router:eth1"]
    - endpoints: ["eng-router:eth2", "eng-host:eth1"]
    - endpoints: ["eng-router:eth3", "lab-host:eth1"]
```

---

## Verification Checklist

Provide students with this checklist. All items must pass for the topology to be considered correct:

```bash
# 1. Library host can reach Engineering host
sudo docker exec clab-campus-lib-host ping -c 3 10.3.0.10

# 2. Admin host can reach Library host
sudo docker exec clab-campus-adm-host ping -c 3 10.1.0.10

# 3. Lab host can reach Library host (via Engineering)
sudo docker exec clab-campus-lab-host ping -c 3 10.1.0.10

# 4. Lab host CANNOT reach Admin directly
#    (should time out if routing policy is correctly enforced)
sudo docker exec clab-campus-lab-host traceroute 10.2.0.10

# 5. Verify routing path from Library to Lab passes through core-router
sudo docker exec clab-campus-lib-host traceroute 10.4.0.10
```

---

## Deliverables

Ask students to submit:

1. `topology.yaml` — the working Containerlab topology file
2. `design.md` — a short document (500–800 words) covering:
   - A diagram of their chosen topology (can be ASCII art or an image)
   - The subnetting scheme they chose and why
   - How they enforced the Lab ↔ Admin isolation requirement
   - One trade-off they made (e.g. single point of failure, why they accepted it)
3. `verification.txt` — copy-paste of the terminal output from running the verification checklist above

---

## Faculty Notes

**Evaluation approach:**
- Deploy the student's `topology.yaml` yourself and run the verification checklist. If it passes, the implementation is correct regardless of design choices.
- The `design.md` is where you assess understanding — a student can get a working topology by trial and error without really understanding why it works.

**Common mistakes:**
- Forgetting `sysctl -w net.ipv4.ip_forward=1` on router nodes — packets are received but not forwarded.
- Missing return routes — packets go one way but replies have nowhere to go.
- Incorrect subnet masks on point-to-point links (using /24 instead of /30 wastes addresses and can cause routing confusion).

**Scaling up:**
- Add a requirement for a **redundant link** (two paths between buildings) to introduce the concept of routing loops and the need for a routing protocol.
- This naturally leads to a follow-on assignment introducing OSPF with a NOS image like Nokia SR Linux.
