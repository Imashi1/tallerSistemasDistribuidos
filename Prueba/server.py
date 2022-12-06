import socket
import _thread
from player import Player
import pickle


class Server:
    def __init__(self):
        self.server = "192.168.1.92"
        self.port = 8000
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listaJugadores = []

    def bindServer(self):
        try:
            self.socket.bind((self.server, self.port))
        except self.socket.error as e:
            print(str(e))

        self.socket.listen(2)
        print("Servidor Inicializado")

    def threadedClient(self,conn, player):
        conn.send(pickle.dumps("recibido"))
        reply = ""
        self.listaJugadores = [Player(self, 192, 160, 'red')]
        while True:
            try:
                
                conn.sendall(pickle.dumps(reply))
            except:
                break
        print("Lost connection")
        conn.close()

    currentPlayer = 0

    def run(self):
        self.bindServer()
        while True:
            conn, addr = self.socket.accept()
            print("Connected to:", addr)
            _thread.start_new_thread(
                self.threadedClient, (self,conn, currentPlayer))
            currentPlayer += 1


if __name__ == '__main__':
    server = Server()
    server.run()
