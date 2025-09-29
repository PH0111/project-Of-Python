import pyfiglet, socket, re



def portScanner(target, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.settimeout(0.8)
    result = server.connect_ex((target, port))
    
    return result

def validIp(target):
    ip = re.findall(r'\b(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b', target)
    if ip:
        return True
    else:
        return False
    
def main():
    open_port = 0
    
    #title
    print(pyfiglet.figlet_format('PORT SCANNER'))

    #chack if ip address are valid
    while True:
        target = input('Enter The Target Ip Address: ')
        if validIp(target):
            print('Valid Ip Address')
            break
        else:
            print('Incorrect IP address!')
    
    #range port
    while True:
        print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
        port = input("Enter port range: ").strip().split('-')
        if int(port[0]) < int(port[1]):
            minPort = int(port[0])
            maxPort = int(port[1])
            break
        else:
            print(f'ERROR: {port[0]} > {port[1]}')
    
    print('\n')
    print('#' * 50)
   
    #start scanning
    print(f'\nScanning {target} Ports {minPort}-{maxPort}\n')
    for port in range(minPort, maxPort):
        result = portScanner(target, port)
        
        if result == 0:
            try:
                service = socket.getservbyport(port)
                print(f' - port {port} open:{service}')
                open_port += 1
            except:
                print(f'port{port} is unknow')
    
    if open_port != 0:
        print(f'There is {open_port} open port')
    else:
        print("No open ports found in the scanned range.")
    

main()
