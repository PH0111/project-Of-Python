import socket, struct, os, subprocess

SERVER = '192.168.1.10'
PORT = 9999
ADDR = (SERVER, PORT)


def clear():
    os.name = subprocess.run(['clear'], check=True)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(cmd):
    client.sendall(cmd.encode('utf-8'))

    #output = client.recv(2048).decode('utf-8')

    


while True:
    clear()
    cmd = input('$: ')
    send(cmd)

    if cmd == 'exit':
        break


client.close()
