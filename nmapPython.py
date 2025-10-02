#!/usr/bin/python

import pyfiglet
import re 
import nmap

#check if the ip addr are valid
def validIp(target):
    ip = re.findall(r'\b(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b', target)
    if ip:
        return True
    else:
        return False



# the main function (HOME)
def main():
    close_port, filtered_port, time_out = 0, 0, 0

    
    #TITLE
    print(pyfiglet.figlet_format('PORT SCANNER'))

    
    #chack if ip address are valid
    while True:
        target = input('Enter The Target Ip Address: ')
        if validIp(target):
            break
        else:
            print(' Incorrect IP address!')
    

    #range port
    while True:
        print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
        port = input("Enter port range: ").strip().split('-')
        if int(port[0]) < int(port[1]):
            minPort = int(port[0])
            maxPort = int(port[1])
            break
        else:
            print(f' ERROR: {port[0]} > {port[1]}')
    
    print('\n')

    #start scanning
    print('Starting the scan on the address {}'.format(target))
    nm = nmap.PortScanner()
    
    for port in range(minPort, maxPort + 1):
        try:
            result = nm.scan(target, str(port))

            time_out += float(result['nmap']['scanstats']['elapsed'])

            port_state = (result['scan'][target]['tcp'][port]['state'])
            port_name = ((result['scan'][target]['tcp'][port]['name']))
        
            if port_state == 'open':
                print(f' - Port {port} open Service: {port_name}')
            if port_state == 'closed':
                close_port += 1
            else:
                filtered_port += 1
        except keyError:
            print('The scan failed')

    print(f'Not Show: \n {close_port} closed ports.\n {filtered_port} filtered ports.')
    
    print(f'\nThe address check is complete in {time_out:.2f} seconds.')


main()
