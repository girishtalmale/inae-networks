# README — Introduction to Containerlab

## Overview

This lab introduces **Containerlab**, a tool used to create, deploy, and manage virtual network topologies using containers. Containerlab allows networking experiments to be performed on a single machine without requiring multiple physical devices.

Instead of configuring several routers, switches, and hosts physically, Containerlab creates lightweight container-based network nodes and interconnects them according to a topology description.

This makes it possible to:

* Build realistic network topologies quickly
* Perform networking experiments safely
* Learn routing, switching, and network protocols
* Test configurations before deployment
* Reproduce experiments consistently

---

# What is Containerlab?

Containerlab is an open-source framework that orchestrates container-based network topologies.

A topology can contain:

* Linux hosts
* Routers
* Switches
* Network appliances
* Custom Docker containers

Containerlab automatically:

* Creates containers
* Connects them using virtual links
* Assigns interfaces
* Builds the desired network topology

A simple topology might look like:

```text
Client ───── Router ───── Server
```

while more complex topologies may contain dozens of interconnected nodes.

---

# Why Use Containerlab?

Containerlab provides several advantages:

### Lightweight

Containers consume significantly fewer resources than virtual machines.

### Fast Deployment

Entire network topologies can be created in seconds.

### Reproducibility

The same topology definition can be deployed repeatedly with identical results.

### Safe Experimentation

Experiments can be performed without affecting production networks.

### Automation Friendly

Topologies can be created, modified, and removed programmatically.

---

# Learning Material

Detailed learning material is available through either of the following methods.

## Option 1 — Hosted Learning Material

Open the following address in a web browser:

```text
10.208.20.119:8888
```

---

## Option 2 — Local Documentation

Open the following file in a web browser:

```text
tutorials/tutorial3/containerlab-site/index.html
```

This documentation contains:

* Containerlab fundamentals
* Topology definitions
* Deployment examples
* Networking concepts
* Practical exercises

---

# Accessing Remote Systems Using SSH

Many Containerlab deployments and networking experiments are performed on remote Linux systems.

SSH (Secure Shell) allows you to securely connect to a remote machine through a terminal.

General syntax:

```bash
ssh username@hostname
```

Example:

```bash
ssh user@10.20.251.231
```

After authentication, commands are executed on the remote system rather than on the local machine.

---

# Checking SSH Availability

## Windows

Open Command Prompt or PowerShell and run:

```powershell
ssh -V
```

Expected output:

```text
OpenSSH_for_Windows_x.x
```

If SSH is available, no additional installation is required.

---

## Optional: Installing PuTTY on Windows

If SSH is unavailable, PuTTY may be installed.

PuTTY provides:

* SSH terminal access
* Saved sessions
* Graphical connection management

However, modern versions of Windows typically include OpenSSH by default, allowing direct use from:

* Command Prompt
* PowerShell
* Windows Terminal

without requiring PuTTY.

---

## macOS

Open Terminal and run:

```bash
ssh -V
```

SSH is included by default on macOS.

No additional software is typically required.

---

## Linux

Most Linux distributions include SSH by default.

Verify using:

```bash
ssh -V
```

---

# Basic Linux Commands

The following commands are frequently used during networking labs.

---

## Display Current Directory

```bash
pwd
```

Example:

```text
/home/user
```

---

## List Files

```bash
ls
```

Detailed listing:

```bash
ls -l
```

---

## Create a Directory

```bash
mkdir my_directory
```

Example:

```bash
mkdir containerlab
```

---

## Change Directory

```bash
cd containerlab
```

Move to parent directory:

```bash
cd ..
```

Move to home directory:

```bash
cd ~
```

---

## Create a File

```bash
touch file.txt
```

---

## Remove a File

```bash
rm file.txt
```

---

# Installing Git

Git is commonly used to obtain lab material and source code.

## Ubuntu/Debian

```bash
sudo apt update
sudo apt install git
```

Verify installation:

```bash
git --version
```

---

# Cloning a Repository

General syntax:

```bash
git clone <repository_url>
```

Example:

```bash
git clone https://github.com/example/repository.git
```

This creates a local copy of the repository.

---

# Creating a Containerlab Topology

Containerlab topologies are described using YAML files.

Example:

```yaml
name: linear

topology:
  nodes:
    client:
      kind: linux

    router:
      kind: linux

    server:
      kind: linux
```

Containerlab reads the topology description and deploys the specified nodes and links.

---

# Executing Commands Inside Containers

After deployment, commands can be executed inside running containers.

Example:

```bash
sudo docker exec clab-linear-client ping -c 4 10.0.2.1
```

---

## Understanding the Command

```bash
sudo docker exec clab-linear-client ping -c 4 10.0.2.1
```

Breakdown:

| Component          | Meaning                                    |
| ------------------ | ------------------------------------------ |
| sudo               | Execute with administrative privileges     |
| docker exec        | Run a command inside an existing container |
| clab-linear-client | Container name                             |
| ping               | Network testing utility                    |
| -c 4               | Send 4 ICMP Echo Requests                  |
| 10.0.2.1           | Destination IP address                     |

The command executes:

```bash
ping -c 4 10.0.2.1
```

inside the container named:

```text
clab-linear-client
```

rather than on the host machine.

---

# Opening an Interactive Shell Inside a Container

Sometimes multiple commands need to be executed inside a container.

Example:

```bash
sudo docker exec -it clab-linear-client sh
```

---

## Understanding the Command

```bash
sudo docker exec -it clab-linear-client sh
```

| Component          | Meaning                          |
| ------------------ | -------------------------------- |
| sudo               | Administrative privileges        |
| docker exec        | Execute command inside container |
| -i                 | Keep STDIN open                  |
| -t                 | Allocate terminal                |
| clab-linear-client | Container name                   |
| sh                 | Launch shell                     |

After execution, the terminal changes into the container environment.

Example:

```text
/ #
```

At this point commands are running inside the container.

Examples:

```bash
ip addr
```

```bash
ip route
```

```bash
ping 10.0.2.1
```

To exit:

```bash
exit
```

---

# Summary

By the end of this lab you should be able to:

* Understand the purpose of Containerlab
* Deploy simple container-based network topologies
* Access remote systems using SSH
* Navigate Linux systems using common commands
* Clone repositories using Git
* Execute commands inside containers
* Open interactive container shells
* Verify connectivity between network nodes

The accompanying Containerlab learning material provides deeper explanations, examples, and exercises for further exploration.
