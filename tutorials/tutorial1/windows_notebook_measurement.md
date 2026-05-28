# README — Notebook Setup for Networking Measurement Lab (Windows)

First download the latest version of the repository using Command Prompt / PowerShell or simply download the repository ZIP from the browser.

```powershell id="q7j0v9"
git clone <REPOSITORY_URL>
cd <REPOSITORY_NAME>
```

Example:

```powershell id="w1i9pr"
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

Open Command Prompt or PowerShell and run:

```powershell id="p3c6j8"
python --version
```

Example output:

```text id="2hn1el"
Python 3.10.12
```

---

# If Python is NOT Installed

Download Python from:

https://www.python.org/downloads/windows/

During installation:

* Enable:

```text id="6r31r5"
Add Python to PATH
```

After installation verify again:

```powershell id="0d99u6"
python --version
pip --version
```

---

# 2. Install Minimal Notebook Setup

Install the required notebook environment and libraries using Command Prompt / PowerShell:

```powershell id="7xg0hf"
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

Inside Command Prompt / PowerShell:

```powershell id="wnkt1p"
code .
```

Create a notebook:

* File → New File
* Save as:

```text id="z4h3n3"
network_measurement_lab.ipynb
```

OR

Use:

* “Create: New Jupyter Notebook”

---

# Running Commands Inside Notebook

Notebook cells can directly execute shell commands using `!`.

Example:

```python id="n7xti8"
!ping google.com
```

Run notebook cells using:

```text id="x5vr8e"
Shift + Enter
```

---

# Option B — Using JupyterLab in Browser

Start JupyterLab using Command Prompt / PowerShell:

```powershell id="0rjw0g"
jupyter lab
```

It will automatically open in your browser.

If it does not open automatically, copy the localhost URL shown in terminal.

Example:

```text id="6byz7r"
http://localhost:8888/lab
```

---

# Create a Notebook in JupyterLab

Inside JupyterLab:

* Click:

```text id="lyklm4"
Python 3
```

under Notebook section.

A new `.ipynb` notebook will open.

---

# Example Notebook Cell

```python id="jfq02r"
print("Notebook setup successful!")
```

Run notebook cells using:

```text id="3p3q2r"
Shift + Enter
```

---

# 4. Install Networking Tools

The following commands should be run in Command Prompt / PowerShell, NOT inside notebook cells.

---

# Ping

Already preinstalled on Windows.

Verify using terminal:

```powershell id="3m3f6g"
ping google.com
```

---

# Traceroute

Windows uses:

```powershell id="1w9z1y"
tracert google.com
```

instead of `traceroute`.

No additional installation required.

---

# iperf3

Download iperf3 Windows binaries from:

https://iperf.fr/iperf-download.php

Extract the downloaded ZIP file.

Open Command Prompt / PowerShell inside the extracted folder.

Verify installation:

```powershell id="l2kg8u"
iperf3.exe --version
```

Optional:

* Add the iperf3 folder to Windows PATH.

---

# 5. Test Commands Inside Notebook

The following examples are intended to be run INSIDE notebook cells.

---

# Ping

```python id="w04t5o"
!ping google.com
```

---

# Traceroute

```python id="snm7dt"
!tracert google.com
```

---

# iperf3

```python id="8xbxzc"
!iperf3.exe <server_ip/dns>
```

If iperf3 is added to PATH:

```python id="d3d3mt"
!iperf3 <server_ip/dns>
```

---

# 6. Useful Notes

* Run notebook cells using:

```text id="d8w6ks"
Shift + Enter
```

* Stop JupyterLab using terminal:

```text id="e6cqzz"
Ctrl + C
```

* Restart notebook kernel if notebook becomes unresponsive.

* Use Command Prompt or PowerShell for all installation commands.

---

# 7. Quick Command Summary

| Tool       | Example Command              |
| ---------- | ---------------------------- |
| ping       | `ping google.com`            |
| traceroute | `tracert google.com`         |
| iperf3     | `iperf3.exe <server_ip/dns>` |

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
