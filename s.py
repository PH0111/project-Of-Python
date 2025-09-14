import socket, threading, shlex

HEADER = 64
PORT = 9999
SERVER = '192.168.1.10'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = {}

def handle_message(msg):
    if msg.startswith('c'):
        arr = shlex.split(msg)
    else:
        arr = []

    return arr

def handle_client(conn, addr, numOfClients):
    clients[f'c{numOfClients}'] = conn

    print(f'[NEW CONNECTION] {addr} connected.')

    connected = True
    while connected:
        msg = conn.recv(HEADER).decode(FORMAT)
        if msg:
            if msg == DISCONNECT_MESSAGE:
                connected = False

            message = handle_message(msg)
            if message:
                recipient_socket = clients.get(message[0])
                if recipient_socket:
                    
                    newMsg = ' '
                    for i in range(1, len(message)):
                        newMsg += message[i] + ' '
                    
                    recipient_socket.send(f'{newMsg}'.encode(FORMAT))
                    print(f'send message to {message[0]}')
            else:
               print(f'[{addr}] {msg}')

            conn.send(f'[{addr[0]}]'.encode(FORMAT))

    conn.close()



def start():
    numOfClients = 0

    print(f'Server connected to [{SERVER}]')
    server.listen()
    while True:   
        conn, addr = server.accept()
        numOfClients += 1
        thread = threading.Thread(target=handle_client, args=(conn, addr, numOfClients))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.active_count() - 1}')

start()
