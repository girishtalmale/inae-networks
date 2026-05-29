# Add Python to PATH on Windows

This guide explains how to add Python to the system PATH on Windows so you can run `python` and `pip` from PowerShell or Command Prompt.

---

# Step 1: Check if Python is Installed

Open PowerShell and run:

```powershell id="t4n2xp"
python --version
```

If you see:

```text id="gu7v3e"
Python is not recognized
```

then Python is either not installed or not added to PATH.

---

# Step 2: Find Python Installation Folder

Typical Python installation paths:

```text id="wj4s0h"
C:\Users\<YOUR_USERNAME>\AppData\Local\Programs\Python\Python310\
```

Scripts folder:

```text id="m2s8kf"
C:\Users\<YOUR_USERNAME>\AppData\Local\Programs\Python\Python310\Scripts\
```

Replace:

```text id="6k9u2a"
<PYOUR_USERNAME>
```

with your Windows username.

---

# Step 3: Open Environment Variables

1. Press:

```text id="s7z4pd"
Windows + S
```

2. Search for:

```text id="6v3a1o"
Environment Variables
```

3. Open:

```text id="5x8lqv"
Edit the system environment variables
```

4. Click:

```text id="5f7o1d"
Environment Variables
```

---

# Step 4: Add Python to PATH

Under **User variables**:

1. Select:

```text id="8n3t9r"
Path
```

2. Click:

```text id="v2f0xq"
Edit
```

3. Click:

```text id="u8w3lp"
New
```

4. Add these two paths:

```text id="m9y4dz"
C:\Users\<YOUR_USERNAME>\AppData\Local\Programs\Python\Python310\
```

```text id="v4h6cs"
C:\Users\<YOUR_USERNAME>\AppData\Local\Programs\Python\Python310\Scripts\
```

5. Click **OK** on all windows.

---

# Step 5: Restart Terminal

Close PowerShell or Command Prompt and reopen it.

---

# Step 6: Verify

Run:

```powershell id="d8x1bn"
python --version
```

and:

```powershell id="t9v6qm"
pip --version
```

Example output:

```text id="z5p8ur"
Python 3.10.0
```

---

# Optional: Install Python Properly

If Python is not installed, download it from:

[Python Official Website](https://www.python.org/downloads/windows/?utm_source=chatgpt.com)

During installation, make sure to check:

```text id="w3j8ka"
Add Python to PATH
```

before clicking Install.


# Install iperf3 on Windows

## Step 1: Download iperf3

Download the Windows binaries from:

[iperf3 Download Page](https://iperf.fr/iperf-download.php?utm_source=chatgpt.com)

---

## Step 2: Extract the ZIP File

After downloading:

1. Right-click the ZIP file
2. Click:

```text id="7j2fvn"
Extract All
```

3. Choose a folder location

---

## Step 3: Open Terminal in the Extracted Folder

Open Command Prompt or PowerShell inside the extracted folder.

### Method 1: Using File Explorer

1. Open the extracted folder
2. Click the address bar
3. Type:

```text id="89a6xb"
powershell
```

or:

```text id="5s8xkc"
cmd
```

4. Press Enter

---

## Step 4: Verify Installation

Run:

```powershell id="1z9gve"
.\iperf3.exe --version
```

Example output:

```text id="1z4ylf"
iperf 3.x
```

---

## Optional: Add iperf3 to PATH

To run `iperf3` from any folder:

1. Copy the extracted folder path
2. Add it to the Windows PATH environment variable
3. Restart PowerShell or Command Prompt

Then you can run:

```powershell id="7d4fkr"
iperf3 --version
```
