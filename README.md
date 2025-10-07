# Keylogger 

## Overview
This repository contains a small Python keylogger implemented for **educational and research** purposes.  
It is intended to help students and researchers study input event handling, forensic logging, and defensive/detection techniques.

> **Disclaimer:** Use only in authorized, controlled environments (VMs, lab machines). Unauthorized deployment or use on systems without explicit consent is illegal and unethical. The author and contributors are not responsible for misuse.


## Requirements
- Python 3.8+  
- Install dependencies:
```bash
pip install pynput pyinstaller
```

## Usage
Run only in a sandboxed environme
```bash
python keylogger.py
```
Captured keystrokes are appended to keylog.txt.

## Build executable
```bash
pyinstaller --onefile keylogger.py
```
Resulting executable will be in the dist/directory.
