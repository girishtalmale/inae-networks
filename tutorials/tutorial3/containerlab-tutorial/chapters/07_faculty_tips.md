# Faculty Tips and Classroom Workflow

This chapter covers practical advice for running Containerlab-based assignments in a course: setting up a shared server, managing student topologies, common troubleshooting steps, and suggestions for scaling up.

---

## Classroom Deployment Models

### Option 1: Shared Department Server (Recommended)

A single Linux server (physical or VM) accessible to all students over SSH is the simplest model for a class. Students deploy their own topologies on the same host; Containerlab's namespace isolation keeps them separate.

**Setup steps:**

1. Install Containerlab on the server (see Chapter 2).
2. Create a Unix account for each student (or use existing university LDAP accounts).
3. Give each student a working directory under `/home/<username>/clab/`.
4. Optionally add students to the `clab_admins` group for sudo-less operation:
   ```bash
   sudo usermod -aG clab_admins <username>
   ```

**Enforcing unique topology names:**

Students sharing a host must use unique topology names to avoid container name collisions. A simple convention:

```yaml
# Student ID: abc123
name: udp-abc123
```

You can enforce this in the assignment spec: *"Your topology name must be your student ID prefixed with the assignment name."*

---

### Option 2: Student Laptops

Each student installs Containerlab on their own machine. Works well for take-home assignments and students comfortable with Linux or WSL.

**Trade-offs:**

| Advantage | Disadvantage |
|---|---|
| No shared resource contention | Setup variability across OS types |
| Students can work offline | Faculty cannot directly inspect student environments |
| Good for learning the tooling | Windows/macOS setup can be time-consuming |

Provide a **setup verification script** students run before the first lab to confirm their environment works:

```bash
#!/bin/sh
# verify-setup.sh
echo "=== Containerlab version ==="
clab version | grep version

echo "=== Docker running ==="
docker info > /dev/null 2>&1 && echo "Docker OK" || echo "Docker NOT running"

echo "=== Deploy test topology ==="
cat > /tmp/verify.yaml << 'EOF'
name: verify
topology:
  nodes:
    n1:
      kind: linux
      image: alpine:latest
      exec:
        - ip addr add 10.99.0.1/24 dev eth1
    n2:
      kind: linux
      image: alpine:latest
      exec:
        - ip addr add 10.99.0.2/24 dev eth1
  links:
    - endpoints: ["n1:eth1", "n2:eth1"]
EOF

sudo clab deploy -t /tmp/verify.yaml > /dev/null 2>&1
RESULT=$(sudo docker exec clab-verify-n1 ping -c 2 -W 1 10.99.0.2 2>&1 | grep "2 received")
sudo clab destroy -t /tmp/verify.yaml > /dev/null 2>&1

[ -n "$RESULT" ] && echo "Setup verified OK" || echo "SETUP FAILED — check Docker and Containerlab"
```

---

### Option 3: GitHub Codespaces

For maximum portability (no local install required), use GitHub Codespaces with the official Containerlab devcontainer image.

1. Create a repository with a `.devcontainer/devcontainer.json`:

```json
{
  "image": "ghcr.io/srl-labs/containerlab/devcontainer:latest",
  "runArgs": ["--privileged", "--network=host"],
  "mounts": [
    "type=bind,src=/var/run/docker.sock,dst=/var/run/docker.sock"
  ]
}
```

2. Students open the repo in Codespaces — Containerlab is available immediately in the browser-based terminal.

This is ideal for assessments and demos but has a monthly free-tier limit on Codespaces compute hours.

---

## Managing Student Topologies

### Listing All Running Topologies on a Shared Server

```bash
sudo clab inspect --all
```

### Cleaning Up a Student's Leftover Topology

If a student forgets to destroy their topology:

```bash
# If you have the topology file
sudo clab destroy -t /home/<student>/clab/topology.yaml

# If you only know the topology name
sudo clab destroy --name <topology-name>

# Nuclear option: destroy all running topologies on the host
sudo clab destroy --all
```

### Resource Limits

On a shared server, set Docker resource limits to prevent one student from consuming all RAM:

```yaml
# In topology.yaml — per node limits
nodes:
  client:
    kind: linux
    image: alpine:latest
    memory: "256m"
    cpu: 0.5
```

---

## Common Troubleshooting

### "Container name already in use"

A topology with the same name is already deployed (possibly from a previous session that wasn't cleaned up).

```bash
sudo clab destroy --name <topology-name>
# Then re-deploy
sudo clab deploy -t topology.yaml
```

### Ping between nodes fails

Check in order:

1. **Are IP addresses assigned?**
   ```bash
   sudo docker exec <container> ip addr show eth1
   ```

2. **Is IP forwarding enabled on router nodes?**
   ```bash
   sudo docker exec <router-container> cat /proc/sys/net/ipv4/ip_forward
   # Should print 1
   ```

3. **Are routes correct?**
   ```bash
   sudo docker exec <container> ip route show
   ```

4. **Is traffic reaching the destination interface?**
   ```bash
   sudo docker exec <server-container> tcpdump -i eth1 icmp -n
   # Then ping from the other node
   ```

### `tc qdisc add` fails: "RTNETLINK answers: File exists"

A tc rule is already applied on that interface. Remove it first:

```bash
sudo docker exec <container> tc qdisc del dev eth1 root
```

### Containers start but `exec` commands failed silently

Check the container logs:

```bash
sudo docker logs clab-<topology>-<node>
```

Exec commands that fail do not cause container startup to fail; they log an error and continue.

---

## Assessment Ideas

### Automated Verification

Write a shell script that deploys a student's topology and runs a checklist of tests. This makes grading fast and objective:

```bash
#!/bin/bash
# grade.sh <topology.yaml>
YAML=$1
TOPO_NAME=$(grep '^name:' $YAML | awk '{print $2}')

sudo clab deploy -t $YAML > /dev/null 2>&1
PASS=0; FAIL=0

check() {
  DESC=$1; CMD=$2; EXPECTED=$3
  RESULT=$(eval $CMD 2>&1)
  if echo "$RESULT" | grep -q "$EXPECTED"; then
    echo "PASS: $DESC"; ((PASS++))
  else
    echo "FAIL: $DESC"; ((FAIL++))
  fi
}

check "lib→server reachable" \
  "sudo docker exec clab-${TOPO_NAME}-lib-host ping -c 2 -W 1 10.3.0.10" \
  "2 packets transmitted, 2 received"

check "lab cannot reach admin directly" \
  "sudo docker exec clab-${TOPO_NAME}-lab-host ping -c 2 -W 1 10.2.0.10" \
  "100% packet loss"

sudo clab destroy -t $YAML > /dev/null 2>&1
echo "Result: $PASS passed, $FAIL failed"
```

### Peer Review

Have students swap topology files and write a short review:
- Does the topology meet the stated requirements?
- Is the subnetting scheme logical and documented?
- What would they change?

This works well because `clab deploy` lets reviewers actually run the topology they are reviewing.

---

## Suggested Course Progression

| Week | Topic | Assignment |
|---|---|---|
| 1 | Install + first topology | Verify setup; deploy linear network; draw a diagram |
| 2 | Subnetting + static routing | Topology design (campus network scenario) |
| 3 | Transport layer basics | UDP sender/receiver; measure loss |
| 4 | Reliability protocols | Stop-and-wait ARQ over UDP |
| 5 | Link conditions | tc netem experiments; throughput vs. loss plots |
| 6 | Advanced | Sliding window ARQ; performance under varying conditions |

---

:::{tip}
Start every lab session with a **10-minute live demo** of deploying and destroying a topology. Students who see the workflow once pick it up quickly, and it sets the expectation that `clab destroy` is always the last step.
:::
