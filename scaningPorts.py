import os, sys, subprocess, re, socket, struct, shlex
#import dns.resolver

try:
    sys.argv[1]
    ip = sys.argv[1]
except:
    print('The target IP address was not found!')
    sys.exit()


target = re.findall(r'\b(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b', ip) #Target Ip Address
if target:
    target = target[0] #Target Ip Address
else:
    print('Incorrect IP address!')
    sys.exit()

open_port = 0

print(f'Scanning {target} ports 1-1000\n')

for p in range(1, 1000):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.settimeout(0.8)
    result = server.connect_ex((target, p))
    
    if result == 0:
        try:
            service = socket.getservbyport(p)
            print(f'  - port {p} is open:{service}')
            open_port += 1
        except:
            print(f' - port {p}:unknown')

        server.close()

if open_port != 0:
    print(f'There is {open_port} open port')
else:
    print("No open ports found in the scanned range.")
