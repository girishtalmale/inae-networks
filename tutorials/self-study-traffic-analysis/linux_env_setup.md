# README — Python Environment Setup for Packet Analysis Lab (Linux)

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

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

Run installer:

```bash
bash Miniconda3-latest-Linux-x86_64.sh
```

Follow installation prompts.

Restart terminal after installation.

Verify installation:

```bash
conda --version
```

---

# 2. Create a Conda Environment

Recommended Python version:

```text
Python 3.10
```

Create environment:

```bash
conda create -n packetlab python=3.10
```

Activate environment:

```bash
conda activate packetlab
```

Verify:

```bash
python --version
```

---

# 3. Alternative: Using Python venv

If you do not want to use Miniconda.

Install Python and venv:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

Create environment:

```bash
python3 -m venv packetlab
```

Activate environment:

```bash
source packetlab/bin/activate
```

Verify:

```bash
python --version
```

---

# 4. Install Required Libraries

Install all required packages:

```bash
pip install dpkt scapy pandas numpy seaborn matplotlib jupyter notebook
```

Verify installation:

```bash
pip list
```

---

# 5. Required Imports

The notebook mentions them

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

```python
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

```python
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

```python
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

```python
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

```python
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

```python
import seaborn as sns
sns.set(color_codes=True)
```

---

# 7. Launch Jupyter Notebook

Start notebook server:

```bash
jupyter notebook
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

```bash
conda activate packetlab
```

OR

```bash
source packetlab/bin/activate
```

Then reinstall missing package.

---

## Scapy Permission Issues

Some packet operations require root privileges.

Example:

```bash
sudo python script.py
```

---

## Jupyter Not Opening

Try:

```bash
jupyter notebook --no-browser
```

Then manually open displayed URL in browser.
