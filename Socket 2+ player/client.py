import socket
host = '192.168.0.6'
port = 8000

ClientSocket = socket.socket()
print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))
Response = ClientSocket.recv(2048)
print (Response)
while True:
    Input = input('Your message: ')
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(2048)
    print(Response.decode('utf-8'))
<<<<<<< Updated upstream
ClientSocket.close()
=======
    print (Response)
ClientSocket.close()
>>>>>>> Stashed changes
