# README — Python Environment Setup for Packet Analysis Lab (Windows)

This guide explains how to:

* Install Miniconda (preferred) or use Python virtual environments (`venv`)
* Create a Python environment
* Install required libraries
* Understand the purpose of each library used in the notebook

The setup is intended for packet/network analysis notebooks using:

* Scapy
* dpkt
* pandas
* numpy
* seaborn

---

# 1. Recommended: Install Miniconda

Miniconda is a lightweight Python distribution and environment manager.

Download Miniconda:

https://docs.conda.io/en/latest/miniconda.html

Download:

* **Miniconda3 Windows 64-bit Installer**

Run the installer and follow setup instructions.

Recommended:

* Enable:

```text id="f1sq4j"
Add Miniconda to PATH
```

After installation, open:

* Command Prompt
  OR
* Anaconda Prompt

Verify installation:

```powershell id="7qgtvr"
conda --version
```

---

# 2. Create a Conda Environment

Recommended Python version:

```text id="0qhtyk"
Python 3.10
```

Create environment:

```powershell id="fy8m7q"
conda create -n packetlab python=3.10
```

Activate environment:

```powershell id="w0imj9"
conda activate packetlab
```

Verify:

```powershell id="35uxk4"
python --version
```

---

# 3. Alternative: Using Python venv

If you do not want to use Miniconda.

---

# Install Python

Download Python from:

https://www.python.org/downloads/windows/

During installation:

* Enable:

```text id="24jlwm"
Add Python to PATH
```

Verify installation:

```powershell id="gdfz61"
python --version
pip --version
```

---

# Create Environment

```powershell id="a7q5ml"
python -m venv packetlab
```

Activate environment:

```powershell id="sx2x6h"
packetlab\Scripts\activate
```

Verify:

```powershell id="5n7k8y"
python --version
```

---

# 4. Install Required Libraries

Install all required packages:

```powershell id="4g7h6j"
pip install dpkt scapy pandas numpy seaborn matplotlib jupyter notebook
```

Verify installation:

```powershell id="9e1h6n"
pip list
```

---

# 5. Required Imports

The notebook mentions them.

---

# 6. Brief Overview of Libraries

---

# dpkt

## Purpose

* Fast packet parsing library
* Reads PCAP files
* Extracts packet headers and protocol information

## Common Usage

* Parse network captures
* Extract TCP/IP fields
* Analyze packets programmatically

## Example

```python id="3v6m2q"
import dpkt
```

---

# Scapy

## Purpose

* Packet manipulation and packet crafting
* Can sniff, create, modify, and send packets

## Common Usage

* Read/write packets
* Create custom packets
* Network experiments
* Protocol analysis

## Example

```python id="l6l5e8"
from scapy.all import *
```

---

# pandas

## Purpose

* Tabular data analysis
* DataFrames for organizing extracted packet information

## Common Usage

* Store packet metadata
* Analyze RTTs
* Aggregate statistics
* CSV processing

## Example

```python id="ltq4iu"
import pandas as pd
```

---

# numpy

## Purpose

* Numerical computations
* Efficient array operations

## Common Usage

* Statistical calculations
* Mathematical operations on packet metrics

## Example

```python id="1qax8k"
import numpy as np
```

---

# binascii

## Purpose

* Convert binary data to ASCII/hexadecimal

## Common Usage

* Decode payloads
* View packet bytes in readable format

## Example

```python id="cg6k2o"
import binascii
```

---

# seaborn

## Purpose

* Statistical plotting library
* Built on top of matplotlib

## Common Usage

* RTT distributions
* Packet size distributions
* Network traffic visualization

## Example

```python id="l4c7x0"
import seaborn as sns
sns.set(color_codes=True)
```

---

# 7. Launch Jupyter Notebook

Start notebook server:

```powershell id="7r5q8v"
python -m jupyterlab
```

This opens Jupyter in browser.

---

# 8. References and Documentation

## dpkt

* Documentation:
  https://dpkt.readthedocs.io/

* GitHub:
  https://github.com/kbandla/dpkt

---

## Scapy

* Documentation:
  https://scapy.readthedocs.io/

* Interactive Tutorial:
  https://scapy.readthedocs.io/en/latest/introduction.html

---

## pandas

* Documentation:
  https://pandas.pydata.org/docs/

* Beginner Tutorial:
  https://pandas.pydata.org/getting_started.html

---

## NumPy

* Documentation:
  https://numpy.org/doc/

* Quickstart:
  https://numpy.org/doc/stable/user/quickstart.html

---

## Seaborn

* Documentation:
  https://seaborn.pydata.org/

* Tutorial:
  https://seaborn.pydata.org/tutorial.html

---

## Jupyter Notebook

* Documentation:
  https://jupyter.org/documentation

---

# 9. Common Troubleshooting

## Module Not Found Error

Ensure correct environment is activated:

```powershell id="fcx6v2"
conda activate packetlab
```

OR

```powershell id="g8vwpi"
packetlab\Scripts\activate
```

Then reinstall missing package.

---

## Scapy Permission Issues

Some packet operations may require administrator privileges.

Example:

* Run Command Prompt as Administrator

---

## Jupyter Not Opening

Try:

```powershell id="lgm2a2"
jupyter notebook --no-browser
```


Then manually open the displayed localhost URL in browser.

---

To install TShark on Windows, the easiest method is to install the full Wireshark package and include TShark during setup.

## Option 1: Install via Wireshark Installer (Recommended)

1. Download the Windows installer from:
   [Wireshark Download Page](https://www.wireshark.org/download.html?utm_source=chatgpt.com)

2. Run the installer.

3. During setup:

   * Keep **TShark** selected (it is enabled by default).
   * Install **Npcap** when prompted (required for packet capture).

4. Finish installation.

5. Open Command Prompt and verify:

```powershell
tshark -v
```

You should see version information.

---

## Add TShark to PATH (if command not found)

If `tshark` is not recognized:

1. Locate installation folder, usually:

```text
C:\Program Files\Wireshark
```

2. Add it to Windows PATH:

   * Search: “Environment Variables”
   * Open **Edit the system environment variables**
   * Environment Variables → Path → Edit → New
   * Add:

```text
C:\Program Files\Wireshark
```

3. Open a new Command Prompt and test again:

```powershell
tshark -v
```

---

## Quick Capture Example

List interfaces:

```powershell
tshark -D
```

Capture packets on interface 1:

```powershell
tshark -i 1
```

Capture only DNS traffic:

```powershell
tshark -i 1 -f "port 53"
```

Save capture:

```powershell
tshark -i 1 -w capture.pcapng
```

Official package info:
[Wireshark Official Site](https://www.wireshark.org?utm_source=chatgpt.com)


---

Authored by Mayank with the use of ChatGPT
