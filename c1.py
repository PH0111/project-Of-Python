import socket


HEADER = 64
PORT = 9999
SERVER = '192.168.1.10'
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
ADDR = (SERVER, PORT)

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    def send(msg):
        message = msg.encode(FORMAT)
       
        client.sendall(message)
        print(client.recv(2048).decode(FORMAT))

    while True:
        m = input('>>> ')
        send(m)

        if m == 'disconnect':
            send(DISCONNECT_MESSAGE)
except:
    print('the sever dones\'t work know.')
