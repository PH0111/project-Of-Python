# Simple Python Port Scanner

This is a simple **TCP port scanner** written in Python.  
It scans the first 1000 TCP ports (1–1000) on a target IP address and prints out which ports are open along with their associated service names (if known).
---

## Features
- Scans ports `1–1000` on a given target.
- Identifies the service name of open ports when available.
- Reports the total number of open ports found.
- Simple to run (no external libraries required).

---

## Requirements
- Python **3.x**
- Standard libraries only (`sys`, `socket`, `re`)

---

## Usage

1. Save the code into a file, for example:  
   nano scanner.py
---

## How to run the code
-python3 scanner.py <target-ip>
-Example
    python3 scanner.py 192.168.1.1
