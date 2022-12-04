import socket
from _thread import *
import sys
#Cambiar por su ip local
server = "192.168.0.15" 
port = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(3)
print("Waiting for a connection, Server Started")

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    #Entrega posición inicial creo (0,0)
    return str(tup[0]) + "," + str(tup[1])

pos = [(0,0),(300,300)]

#client_handler
def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    print('j1')
                    reply = pos[0]

                else:
                    #print('j3')
                    print('j2')
                    #reply = pos[2]
                    reply = pos[1]

                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(str.encode(make_pos(reply)))
        except:
            break
    
    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1

    '''
    elif player == 2:
        print('j2')
        reply = pos[1]
    '''