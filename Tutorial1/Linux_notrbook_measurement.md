# VS Code Notebook Setup for Networking Lab (Linux)

This guide helps set up:

* Visual Studio Code (VS Code)
* Jupyter Notebook support inside VS Code
* Networking tools:

  * `ping`
  * `traceroute`
  * `iperf3`

This lab uses shell commands only and does not require a Python virtual environment.

---

# 1. Install VS Code (Optionally)

## Ubuntu / Debian

Open terminal and run:

```bash
sudo apt update
sudo apt install wget gpg

wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg

sudo install -D -o root -g root -m 644 packages.microsoft.gpg \
/etc/apt/keyrings/packages.microsoft.gpg

echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/packages.microsoft.gpg] \
https://packages.microsoft.com/repos/code stable main" | \
sudo tee /etc/apt/sources.list.d/vscode.list

sudo apt update
sudo apt install code
```

Launch VS Code:

```bash
code
```

---

# 2. Install Python and Jupyter Support

Check if Python is installed:

```bash
python3 --version
```

If not installed:

```bash
sudo apt install python3 python3-pip
```

Install Jupyter:

```bash
pip3 install notebook jupyter
```

---

# 3. Install VS Code Extensions

Open VS Code.

Go to:

* Extensions (`Ctrl + Shift + X`)

Install:

1. Python
2. Jupyter

Both are published by Microsoft.

---

# 4. Open a Notebook

Create a working directory:

```bash
mkdir network_lab
cd network_lab
```

Open in VS Code:

```bash
code .
```

Create notebook:

* File → New File
* Save as:

```text
network_measurement.ipynb
```

OR

Use:

* “Create: New Jupyter Notebook”

---

# 5. Running Shell Commands in Notebook

Notebook cells can directly execute shell commands using `!`.

Example:

```python
!ping -c 4 google.com
```

---

# 6. Install Networking Tools

## Ping

Usually preinstalled.

Check:

```bash
ping google.com
```

---

## Traceroute

Install:

```bash
sudo apt install traceroute
```

Verify:

```bash
traceroute google.com
```

---

## iperf3

Install:

```bash
sudo apt install iperf3
```

Verify:

```bash
iperf3 --version
```

---

# 7. Test Commands Inside Notebook

## Ping

```python
!ping -c 5 google.com
```

---

## Traceroute

```python
!traceroute google.com
```

---

## iperf3

```python
!iperf3 --version
```

---

# 8. Basic iperf3 Usage

## Start Server

```bash
iperf3 -s
```

---

## Connect Client

```bash
iperf3 -c SERVER_IP
```

---

# 9. Recommended Folder Structure

```text
network_lab/
│
├── network_measurement.ipynb
├── screenshots/
└── notes/
```

---

# 10. Useful Notes

* Run notebook cells using:

```text
Shift + Enter
```

* Restart kernel if notebook becomes unresponsive.
* Some networking commands may require `sudo`.

Example:

```bash
sudo traceroute google.com
```

---

# 11. Quick Command Summary

| Tool          | Example Command         |
| ------------- | ----------------------- |
| ping          | `ping -c 5 google.com`  |
| traceroute    | `traceroute google.com` |
| iperf3 server | `iperf3 -s`             |
| iperf3 client | `iperf3 -c SERVER_IP`   |
