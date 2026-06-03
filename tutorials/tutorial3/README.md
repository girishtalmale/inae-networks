# README — GitHub Codespaces and Containerlab Setup

## Overview

This lab uses **GitHub Codespaces** to provide a consistent Linux development environment and **Containerlab** to build and experiment with virtual network topologies.

Before starting the Containerlab exercises, create a personal copy of the repository and launch a GitHub Codespace.

Repository:

```text
https://github.com/Mayankonweb/container-labs/
```

> **Important:** This repository does not contain the actual lab material. Its purpose is to provide a pre-configured GitHub Codespaces environment so that everyone can start with a consistent setup without spending time installing software or configuring dependencies locally.

---

# What is GitHub?

GitHub is a cloud platform built around Git that allows developers to:

* Store code online
* Track changes over time
* Collaborate with others
* Manage project history
* Share and reproduce projects

GitHub is widely used in industry, research, and open-source software development.

---

# Why Use GitHub?

GitHub provides:

### Version Control

Track every change made to files and projects.

### Collaboration

Allow multiple people to work on the same project.

### Backup

Store code safely in the cloud.

### Reproducibility

Share projects and environments easily.

### Development Environments

Services such as GitHub Codespaces provide ready-to-use cloud development environments.

---

# Learning Resources

To learn more about Git and GitHub:

### GitHub Skills

https://skills.github.com

### GitHub Documentation

https://docs.github.com

### Introduction to GitHub

https://docs.github.com/en/get-started/start-your-journey/about-github-and-git

### Git Documentation

https://git-scm.com/doc

---

# Step 1 — Create a GitHub Account

If you do not already have a GitHub account, create one at:

```text
https://github.com
```

GitHub accounts are free for personal and educational use.

---

# Step 2 — Fork the Repository

Open the link:

```text
https://github.com/Mayankonweb/container-labs/fork
```



A fork creates a copy of the repository under your GitHub account.

Example:

```text
Original Repository:
Mayankonweb/container-labs

Your Fork:
your-username/container-labs
```

This allows you to:

* Create your own Codespace
* Save your work independently
* Experiment freely without affecting the original repository

---

# What is GitHub Codespaces?

GitHub Codespaces is a cloud-based development environment provided by GitHub.

Each Codespace provides:

* Linux environment
* VS Code in the browser
* Terminal access
* Pre-installed development tools
* Persistent workspace

Conceptually:

```text
Your Browser
      │
      ▼
GitHub Codespace
      │
      ▼
Linux Machine in the Cloud
```

Instead of installing software locally, you work directly inside a cloud-hosted Linux machine.

---

# Why Use GitHub Codespaces?

Codespaces simplify setup significantly.

Advantages include:

* No local software installation
* Consistent environment across systems
* Browser-based development
* Integrated terminal
* GitHub integration
* Easy access from any machine

---

# Step 3 — Create a Codespace

After creating your fork:

1. Open your forked repository.
2. Click the green **Code** button.
3. Select the **Codespaces** tab.
4. Click **Create codespace on main**.

GitHub will create and start a cloud development environment.

The first launch may take a few minutes.

---

# Step 4 — Verify the Environment

Once the Codespace opens, open the integrated terminal and run:

```bash
pwd
```

```bash
ls
```

You should see the contents of your forked repository.

---

# Working Inside the Codespace

The Codespace provides:

* File explorer
* VS Code editor
* Integrated terminal
* Git integration
* Linux shell environment

Example commands:

```bash
mkdir test
```

```bash
cd test
```

```bash
git status
```

```bash
python --version
```

---

# Introduction to Containerlab

Containerlab is an open-source framework used to create, deploy, and manage container-based network topologies.

Instead of requiring multiple physical routers, switches, and hosts, Containerlab creates lightweight virtual network devices using containers.

A simple topology might look like:

```text
Client ───── Router ───── Server
```

Containerlab automatically:

* Creates containers
* Connects network links
* Assigns interfaces
* Deploys complete network topologies

---

# Why Use Containerlab?

Containerlab provides several advantages.

### Lightweight

Containers consume significantly fewer resources than virtual machines.

### Fast Deployment

Network topologies can be created within seconds.

### Reproducibility

The same topology can be recreated repeatedly.

### Safe Experimentation

Experiments can be performed without affecting production systems.

### Automation Friendly

Topologies can be created and removed programmatically.

---

# Containerlab Learning Material

Detailed learning material is available through either of the following methods.

## Option 1 — Hosted Documentation

Open:

```text
10.208.20.119:8888
```

in a web browser.

---

## Option 2 — Local Documentation

Open the following file in a web browser:

```text
tutorials/tutorial3/containerlab-site/index.html
```

The documentation contains:

* Containerlab fundamentals
* Topology definitions
* Deployment examples
* Networking concepts
* Practical exercises

---

# Basic Linux Commands

These commands are frequently used throughout the labs.

## Current Directory

```bash
pwd
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

## Create Directory

```bash
mkdir my_directory
```

---

## Change Directory

```bash
cd my_directory
```

Parent directory:

```bash
cd ..
```

Home directory:

```bash
cd ~
```

---

## Create File

```bash
touch file.txt
```

---

## Remove File

```bash
rm file.txt
```

---

# Installing Git (Optional)

Git is usually pre-installed in GitHub Codespaces.

On Ubuntu or Debian systems:

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
git clone <repository-url>
```

Example:

```bash
git clone https://github.com/example/repository.git
```

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

Containerlab reads the topology file and deploys the specified network.

---

# Executing Commands Inside Containers

Example:

```bash
sudo docker exec clab-linear-client ping -c 4 10.0.2.1
```

This command executes:

```bash
ping -c 4 10.0.2.1
```

inside the container:

```text
clab-linear-client
```

rather than on the host machine.

---

# Opening an Interactive Container Shell

Example:

```bash
sudo docker exec -it clab-linear-client sh
```

Breakdown:

| Component          | Meaning                          |
| ------------------ | -------------------------------- |
| sudo               | Administrative privileges        |
| docker exec        | Execute command inside container |
| -i                 | Keep STDIN open                  |
| -t                 | Allocate terminal                |
| clab-linear-client | Container name                   |
| sh                 | Launch shell                     |

After execution, you are operating inside the container.

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

Exit using:

```bash
exit
```

---

# Summary

Before beginning the Containerlab exercises:

* Create a GitHub account
* Fork the repository
* Create a GitHub Codespace from your fork
* Verify terminal access
* Familiarize yourself with basic Linux commands
* Review the Containerlab learning material

After completing these steps, you will be ready to deploy and experiment with Containerlab network topologies in a consistent cloud-based Linux environment.
