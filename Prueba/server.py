import socket
from _thread import *

host = ""
port = 8000

def accept_connections(ServerSocket):
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(client_handler, (Client, ))

def abrirServidor(host,port):
    socketServer = socket.socket()
    try: 
        socketServer.bind((host, port))
    except socket.error as e:
        print(str(e))
    print(f'Servidor esta alojando en el puerto {port}...')
    socketServer.listen()

    while True:
        accept_connections(socketServer)
abrirServidor(host, port)