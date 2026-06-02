# Installing Containerlab

Containerlab can be installed on **Linux**, **macOS**, and **Windows**. Linux is the native platform; macOS and Windows require a Linux layer underneath, but the workflow is nearly identical once set up.

---

## Prerequisites (All Platforms)

- **Docker** must be installed and running
- **sudo / administrator privileges**
- A terminal (bash, zsh, or PowerShell for Windows)

---

## Linux Installation

Linux is the recommended platform for both faculty machines and department servers. Containerlab is distributed as a native `.deb` / `.rpm` / `.apk` package.

### Quick Install (Recommended)

Run the official one-line setup script:

```bash
curl -sL https://containerlab.dev/setup | sudo -E bash -s "all"
```

This installs Docker (if not already present) and the latest Containerlab release in one step.

### Verify the Installation

```bash
clab version
```

You should see output like:

```
                           _                   _       _
                 _        (_)                 | |     | |
 ____ ___  ____ | |_  ____ _ ____  ____  ___ | | ____| | _
/ ___) _ \|  _ \|  _)/ _  | |  _ \|  _ \/ _ \| |/ _  | || \
( (__| |_|| | | | |_( ( | | | | | | | | | |_| | ( ( | | |_) )
\____)___/|_| |_|\___)_||_|_|_| |_|_| |_|\___/|_|\_||_|____/

    version: 0.75.0
```

### Supported Distributions

Containerlab works on any Debian-based (Ubuntu, Debian, Linux Mint) or RHEL-based (RHEL, CentOS, Rocky Linux, Fedora, Amazon Linux) distribution on `amd64` or `arm64` architectures.

---

## macOS Installation

macOS is not Linux, so Containerlab cannot run natively. The recommended approach is to use **OrbStack** — a fast, lightweight Linux VM manager — to host a Linux environment in which Containerlab runs natively.

### Step 1: Install OrbStack

Download and install OrbStack from [orbstack.dev](https://orbstack.dev). It is free for personal use.

OrbStack provides both Docker Desktop integration and the ability to spin up full Linux VMs with a single command.

### Step 2: Create a Linux VM

```bash
orb create ubuntu clab
```

This creates an Ubuntu VM named `clab` managed by OrbStack.

### Step 3: Enter the VM and Install Containerlab

```bash
orb shell clab
curl -sL https://containerlab.dev/setup | sudo -E bash -s "all"
```

### Step 4: Verify

```bash
clab version
```

### Notes for macOS

- All `clab` commands are run **inside** the OrbStack VM, not in a macOS terminal directly.
- Your macOS home directory is automatically mounted inside the VM, so you can edit topology files with your favourite macOS editor and deploy them from the VM shell.
- The following NOS kinds work well on Apple Silicon: Nokia SR Linux, Arista cEOS (ARM version), Cisco IOL (via Rosetta emulation).

---

## Windows Installation

Containerlab on Windows runs inside **WSL 2** (Windows Subsystem for Linux).

### Step 1: Enable WSL 2

Open PowerShell as Administrator and run:

```powershell
wsl --install
```

Restart your machine when prompted.

### Step 2: Install a Linux Distribution

```powershell
wsl --install -d Ubuntu
```

### Step 3: Open the WSL Terminal and Install Containerlab

```bash
curl -sL https://containerlab.dev/setup | sudo -E bash -s "all"
```

### Step 4: Verify

```bash
clab version
```

### Notes for Windows

- All topology files and `clab` commands live inside the WSL environment.
- Docker Desktop for Windows can be configured to integrate with WSL 2 — this is the recommended Docker backend.
- Students using Windows should be guided to set up WSL 2 before the first lab session.

---

## Recommended Classroom Setup

For a course, consider one of these models:

| Model | Description | Best For |
|---|---|---|
| **Shared lab server** | One Linux server per class; students SSH in | Larger classes, resource-intensive NOS images |
| **Student laptops** | Each student installs on their own machine | Smaller classes, take-home assignments |
| **GitHub Codespaces** | Containerlab devcontainer in the cloud | No local install required; works from any browser |

:::{tip}
**Shared server** is usually the easiest for faculty to manage. Give each student their own directory and let them deploy/destroy their own topologies. Students share the host kernel but their topologies are fully isolated.
:::

---

## Testing Your Installation

Once installed (on any platform), deploy the built-in example topology to confirm everything works:

```bash
# Create a test topology file
cat > test.yaml << 'EOF'
name: test

topology:
  nodes:
    n1:
      kind: linux
      image: alpine:latest
    n2:
      kind: linux
      image: alpine:latest

  links:
    - endpoints: ["n1:eth1", "n2:eth1"]
EOF

# Deploy
sudo clab deploy -t test.yaml

# List running nodes
sudo clab inspect -t test.yaml

# Ping from n1 to n2 (check the IP from inspect output)
sudo docker exec -it clab-test-n1 ping -c 3 <n2-ip>

# Tear down
sudo clab destroy -t test.yaml
```

If the ping succeeds, your Containerlab installation is working correctly.
