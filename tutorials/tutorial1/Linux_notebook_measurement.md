# README — Notebook Setup for Networking Measurement Lab (Linux)

First download the latest version of the repository using terminal or just use simple download using web browser.

```bash id="7tgr3m"
git clone <REPOSITORY_URL>
cd <REPOSITORY_NAME>
```

Example:

```bash id="8vr7pd"
git clone https://github.com/tarunmangla/inae-networks
cd inae-networks
```

---

This guide helps you set up:

* Jupyter Notebooks
* Visual Studio Code (VS Code)
* Required Python libraries
* Networking lab notebook environment

The easiest setup uses:

* `pip`
* JupyterLab
* VS Code Jupyter extension (optional)

---

# 1. Check Python Installation

First verify whether Python is already installed.

Open terminal and run:

```bash id="8b54hr"
python3 --version
```

Example output:

```text id="m5hl7l"
Python 3.10.12
```

---

# If Python is NOT Installed

Install Python and pip using terminal:

```bash id="8kz8c1"
sudo apt update
sudo apt install python3 python3-pip
```

Verify installation again:

```bash id="5pq2dr"
python3 --version
pip3 --version
```

---

# 2. Install Minimal Notebook Setup

Install the required notebook environment and libraries using terminal:

```bash id="4e9r0v"
pip install jupyterlab pandas matplotlib
```

This installs:

* JupyterLab
* Pandas
* Matplotlib

---

# 3. Choose How You Want to Use Notebooks

You can use notebooks in two ways:

## Option A — Using VS Code 

OR

## Option B — Using JupyterLab in Browser

---

# Option A — Using VS Code

If VS Code is already installed:

Open VS Code.

Go to:

* Extensions (`Ctrl + Shift + X`)

Install these extensions:

1. Python
2. Jupyter

Both are published by Microsoft.

---

# Open the Notebook

Inside terminal:

```bash id="f6k0z5"
code .
```

Create a notebook:

* File → New File
* Save as:

```text id="rlj7qn"
network_measurement_lab.ipynb
```

OR

Use:

* “Create: New Jupyter Notebook”

---

# Running Commands Inside Notebook

Notebook cells can directly execute shell commands using `!`.

Example:

```python id="x0r5ie"
!ping -c 4 google.com
```

Run notebook cells using:

```text id="2dnckd"
Shift + Enter
```

---

# Option B — Using JupyterLab in Browser

Start JupyterLab using terminal:

```bash id="st8bf7"
python -m jupyterlab
```

It will automatically open in your browser.

If it does not open automatically, copy the localhost URL shown in terminal.

Example:

```text id="d1dnfq"
http://localhost:8888/lab
```

---

# Create a Notebook in JupyterLab

Inside JupyterLab:

* Click:

```text id="7gct1g"
Python 3
```

under Notebook section.

A new `.ipynb` notebook will open.

---

# Example Notebook Cell

```python id="zupn7z"
print("Notebook setup successful!")
```

Run notebook cells using:

```text id="z2t62r"
Shift + Enter
```

---

# 4. Install Networking Tools

The following commands should be run in terminal, NOT inside notebook cells.

---

# Ping

Usually preinstalled.

Verify using terminal:

```bash id="c2yctg"
ping google.com
```

---

# Traceroute

Install using terminal:

```bash id="jlwm9k"
sudo apt install traceroute
```

Verify using terminal:

```bash id="1n6yba"
traceroute google.com
```

---

# iperf3

Install using terminal:

```bash id="hs0o5o"
sudo apt install iperf3
```

Verify using terminal:

```bash id="mf01i6"
iperf3 --version
```

---

# 5. Test Commands Inside Notebook

The following examples are intended to be run INSIDE notebook cells.

---

# Ping

```python id="2tbjje"
!ping -c 5 google.com
```

---

# Traceroute

```python id="s56s87"
!traceroute google.com
```

---

# iperf3

```python id="tyt5jg"
!iperf3 <server_ip/dns>
```

---

# 6. Useful Notes

* Run notebook cells using:

```text id="rq0i91"
Shift + Enter
```

* Stop JupyterLab using terminal:

```text id="4c4v4e"
Ctrl + C
```

* Restart notebook kernel if notebook becomes unresponsive.

* Some networking commands may require terminal permissions using `sudo`.

Example:

```bash id="jlwmq0"
sudo traceroute google.com
```

---

# 7. Quick Command Summary

| Tool       | Example Command         |
| ---------- | ----------------------- |
| ping       | `ping -c 5 google.com`  |
| traceroute | `traceroute google.com` |
| iperf3     | `iperf3 <server_ip/dns>`|

---

# References

* Jupyter Documentation
  https://docs.jupyter.org/en/latest/

* JupyterLab Documentation
  https://jupyterlab.readthedocs.io/en/stable/

* VS Code Python Extension
  https://marketplace.visualstudio.com/items?itemName=ms-python.python

* VS Code Jupyter Extension
  https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter

---

Authored by Mayank with the use of ChatGPT
