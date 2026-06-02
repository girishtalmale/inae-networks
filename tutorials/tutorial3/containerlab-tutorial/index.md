# Containerlab: A Faculty Guide to Network Assignment Design

Welcome to this hands-on guide for faculty who want to design and deliver **network programming and networking assignments** using [Containerlab](https://containerlab.dev/) — a free, open-source tool for creating virtual network topologies with containers.

---

## Who Is This Guide For?

This tutorial is written for **faculty with little or no prior Containerlab experience** who want to:

- Set up Containerlab on their own machine or a department server
- Understand what kinds of assignments Containerlab enables
- Design, deploy, and tear down lab environments for students
- Create assignments around real networking concepts using isolated, reproducible topologies

No prior Docker or Linux networking expertise is assumed, though basic comfort with the command line will help.

---

## What You Will Learn

This guide walks you through:

1. **What Containerlab is** and why it is well-suited for teaching
2. **Installing Containerlab** on Linux, macOS, and Windows
3. **Your first topology** — deploying a simple two-node network
4. **Assignment: TCP-like reliability over UDP** — building a custom transport layer
5. **Assignment: Network topology design** — students design and justify network architectures
6. **Assignment: Dynamic link conditions** — simulating packet loss, delay, and bandwidth limits
7. **Faculty tips** — classroom workflow, student access patterns, troubleshooting

---

## Why Containerlab for Teaching?

| Feature | Benefit for Teaching |
|---|---|
| **Free and open-source** | No licensing cost for department or students |
| **Container-based** | Lightweight — dozens of nodes on a single laptop |
| **Declarative topology files** | Students submit a single YAML file as their "network design" |
| **Reproducible** | `clab deploy` and `clab destroy` give clean environments every run |
| **Real Linux networking** | Students use actual `ip`, `tc`, `ping`, `tcpdump` — not simulations |
| **Cross-platform** | Works on Linux, macOS (via VM), and Windows (via WSL2) |

---

:::{note}
All topology files and code snippets in this guide are ready to copy and use. Each assignment chapter includes a suggested learning objective, setup instructions, and discussion questions for students.
:::

Let's get started →
