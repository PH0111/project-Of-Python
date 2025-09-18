# Remote Command Server

This project is a simple Python server that accepts TCP connections and executes commands sent from a client.

## Features
- Listens on a specific IP and port (default: 192.168.1.10:9999).
- Executes shell commands received from the client.
- Supports changing directories using `cd <path>`.
- Closes the session when the client sends `exit`.
--

## Files
- `server.py` — the server script (example implementation).
- `client.py` — recommended simple client to connect and send commands (optional).
- `README.md` — this file.

--

## How It Works
1. Start the server on your PC.
2. Connect with a client (e.g., another Python script or netcat).
3. Send commands to the server.
   - Example: `ls`, `pwd`, `whoami`, etc.
   - Change directory: `cd /path/to/dir`
   - Close session: `exit`

## Requirements
- Python 3.x
- Runs on Linux / Windows

## Disclaimer
⚠️ This code executes commands directly on the host machine.
Use it for **educational purposes only** and only on systems you own.
Do **NOT** expose it to the internet for security reasons.

---

## Usage

1. Edit `server.py` to set the desired `SERVER` IP and `PORT`. Example defaults are:
   ```py
   SERVER = '192.168.1.10'
   PORT = 9999
