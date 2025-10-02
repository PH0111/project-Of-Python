# PORT SCANNER

A simple interactive Python port scanner script that uses `nmap` via the `python-nmap` package to scan a range of TCP ports on a target IPv4 address. The script prints an ASCII title (via `pyfiglet`), asks for a target IP and a port range, scans each port in the range using `nmap.PortScanner()`, and reports open ports as well as a short summary.

---

## Features

- Interactive prompt to enter a target IPv4 address.
- Interactive prompt to enter a port range in the form `min-max` (for example `60-120`).
- Uses `pyfiglet` to print a big `PORT SCANNER` banner.
- Uses the `python-nmap` wrapper to run `nmap` scans programmatically and extract port state and service names.
- Prints open ports and a short summary of closed/filtered ports and elapsed time.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3 (the script uses the `python3` shebang)
- `nmap` (the system `nmap` binary must be installed and available in your PATH)
- Python packages (installable via `pip`):
  - `python-nmap` (this is the `nmap` library used by the script; package name on PyPI: `python-nmap`)
  - `pyfiglet`

Install the Python packages with pip, for example:

```bash
pip3 install python-nmap pyfiglet
```

Install the system `nmap` (on Debian/Ubuntu):

```bash
sudo apt update && sudo apt install nmap
```

You may need to run scans with elevated privileges for certain scan types and port ranges; if you encounter permission issues, try running the script with `sudo`.

---

## Usage

1. Make the script executable (if necessary):

```bash
chmod +x port_scanner.py
```

2. Run the script:

```bash
./port_scanner.py
# or
python3 port_scanner.py
```

3. When prompted, enter the target IPv4 address. The script validates the format using a regular expression and will reject invalid addresses.

4. When prompted for a port range, provide it in the form `min-max` (e.g. `60-120`). The script expects `min < max` and will print an error if the first number is greater than or equal to the second.

Example interaction:

```
Enter The Target Ip Address: 192.168.1.10
Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)
Enter port range: 20-1024
Starting the scan on the address 192.168.1.10
 - Port 22 open Service: ssh
 - Port 80 open Service: http
Not Show:
  15 close ports.
  100 filtered ports.

The address check is complete in 2.34 seconds.
```

---

## Output explanation

- The script prints open ports along with the service name reported by `nmap`.
- At the end it prints a small summary showing counts of closed and filtered ports and the total elapsed time reported by `nmap`.
