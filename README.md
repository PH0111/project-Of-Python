# Port Scanner

A small, terminal-based port scanner written in Python. It prints an ASCII title using `pyfiglet`, validates the target IPv4 address with a regular expression, accepts a port range from the user, and checks which ports in that range are open on the target host using TCP connect attempts.

---

## Features

* Simple TCP port scanning using `socket.connect_ex()` with a short timeout.
* IPv4 address validation using a regular expression.
* Looks up common service names for open ports via `socket.getservbyport()`.
* Nicely formatted terminal title using `pyfiglet`.

## Requirements

* Python 3.7+ (or any modern Python 3.x)
* Python packages:

* `pyfiglet` (install with `pip install pyfiglet`)
* Standard library: `socket`, `re` (note: the provided code expects `re` to be available)

## Installation

1. Ensure you have Python 3 installed.
2. Install `pyfiglet`:

```bash
pip install pyfiglet
```

3. Save the scanner script to a file, e.g. `scanner.py`.

> **Note:** The example code uses `re` in `validIp()` but does not show an `import re` statement. Make sure `import re` is present at the top of the script, otherwise the script will raise a `NameError`.

## Usage

The script will prompt for:

1. **Target IP address** — Enter a valid IPv4 address (the script validates the format with a regex).
2. **Port range** — Enter the range in the format `min-max` (for example: `60-120`).

The script then scans ports from `min` (inclusive) up to `max` (exclusive) and prints which ports are open. Example interaction:

```
PORT SCANNER (ASCII title)
Enter The Target Ip Address: 192.168.1.10
Valid Ip Address
Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)
Enter port range: 20-1024

Scanning 192.168.1.10 Ports 20-1024
 - port 22 open:ssh
port23 is unknow
...
There is 2 open port
```

### Important behavior details

* The code uses `range(minPort, maxPort)` so **the `max` value is excluded** from the scan. If you want to include `max`, enter `max + 1` or update the code.
* The script uses a socket timeout of `0.8` seconds for each connection attempt — you can increase this if scanning a slow remote host.
* `socket.getservbyport(port)` is used to attempt to resolve the service name; it may raise if the port has no registered service in the system database (the script catches this and prints a fallback message).

## Known issues & suggestions

* **No validation of numeric ranges:** The script assumes the user enters integers and that `0 <= min < max <= 65535`. Consider adding checks to enforce valid port numbers.
* **Range inclusivity:** The `max` is exclusive. Either document or change the loop to `range(minPort, maxPort + 1)` if you want inclusive behavior.
* **Concurrency:** Scanning ports sequentially is slow for large ranges. Consider using threading or asynchronous sockets to speed up scans.
* **More informative output:** The script prints `port{port} is unknow` (typo and formatting). You may want to standardize output and fix typos.
* **Graceful interrupts:** Add keyboard interrupt handling (`try/except KeyboardInterrupt`) to stop the scan cleanly.

## Security & Ethics

Only scan hosts you are authorized to test. Port scanning can be considered intrusive and may trigger intrusion-detection systems or legal consequences when performed without permission.

## License

This README and the accompanying scanner script are provided under the MIT License. Use at your own risk.
