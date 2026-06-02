# What Is Containerlab?

## The Core Idea

Containerlab is an open-source tool that lets you spin up **virtual network topologies** using Linux containers. Instead of buying physical switches and routers — or fighting with heavyweight VM-based simulators — you describe your desired network in a simple YAML file, run one command, and your network is live in seconds.

Think of it as `docker-compose`, but for **networks**: nodes are containers, and the links between them are virtual Ethernet cables that Containerlab wires up automatically.

---

## How It Works

A Containerlab topology has two ingredients:

1. **Container images** — each node in the network runs as a Docker container. This can be a plain Linux Alpine container, a router image like Nokia SR Linux or Arista cEOS, or your own custom image.
2. **A topology file (`.yaml`)** — a human-readable file that declares the nodes and the links between them.

When you run `sudo clab deploy -t topology.yaml`, Containerlab:

- Pulls any missing container images
- Creates and starts the containers
- Wires up virtual Ethernet links between them
- Assigns management IP addresses
- Writes an SSH config so you can log in to any node by name

When you are done, `sudo clab destroy -t topology.yaml` tears everything down cleanly.

---

## A Minimal Example

Here is what a two-node topology file looks like:

```yaml
name: hello-clab

topology:
  nodes:
    client:
      kind: linux
      image: alpine:latest

    server:
      kind: linux
      image: alpine:latest

  links:
    - endpoints: ["client:eth1", "server:eth1"]
```

That is the entire file. Running `sudo clab deploy -t hello-clab.yaml` gives you two Alpine Linux containers connected by a virtual Ethernet link, ready for students to experiment with.

---

## Why It Is Good for Teaching

### Real Linux Networking
Students use real kernel tools: `ip`, `ping`, `traceroute`, `tcpdump`, `iperf3`, `tc` (traffic control). There is no abstraction layer hiding what is happening — what students see is what actually happens on a network.

### Isolation and Reproducibility
Each deployment is isolated. A student cannot accidentally break another student's topology. `clab destroy` followed by `clab deploy` gives a completely fresh environment in seconds — ideal when students need to reset after a mistake.

### Assignments as Code
A topology file is just a text file. Students submit it to a version-control system, instructors diff it to see changes, and anyone can reproduce the exact same network by running one command. This makes grading and peer review straightforward.

### Lightweight
A simple two- or three-node topology of Alpine Linux containers uses only a few hundred megabytes of RAM. A modest server or even a faculty laptop can host enough environments for a full class.

---

## Key Concepts Glossary

| Term | Meaning |
|---|---|
| **Node** | A container acting as a network device (router, host, switch, etc.) |
| **Link** | A virtual Ethernet cable connecting two node interfaces |
| **Kind** | The type of node (e.g. `linux`, `srl` for Nokia SR Linux, `ceos` for Arista) |
| **Topology file** | The YAML file describing nodes and links |
| **Management network** | A separate Docker network Containerlab creates for SSH access to all nodes |
| **`clab deploy`** | Command to start a topology |
| **`clab destroy`** | Command to tear down a topology |
| **`clab inspect`** | Command to view running topologies and management IPs |

---

:::{tip}
For the assignments in this guide, we exclusively use the `linux` kind with standard Alpine or Ubuntu images. This means students do **not** need any vendor-specific NOS images, and there are no licensing concerns.
:::
