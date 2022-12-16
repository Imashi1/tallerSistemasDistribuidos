import socket
from threading import Thread
from zlib import compress

from mss import mss

WIDTH = 1920
HEIGHT = 1080



def capturar_pantalla(conn):
    #Captura de pantallazos continuos
    with mss() as sct:
        #Región a tomar capturas
        rect = {'top': 0, 'left': 0, 'width': WIDTH, 'height': HEIGHT}

        while 'recording':
            #Compresión de imagenes
            img = sct.grab(rect)
            pixels = compress(img.rgb, 6)

            size = len(pixels)
            size_len = (size.bit_length() + 7) // 8
            #Envía largo de pixeles
            conn.send(bytes([size_len]))

            #Envía tamaño bytes
            size_bytes = size.to_bytes(size_len, 'big')
            conn.send(size_bytes)

            conn.sendall(pixels)

def main():
    #Inicia el servidor
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("192.168.1.92", 5555))
    try:
        sock.listen(5)
        print('Servidor Iniciado')

        while 'connected':
            conn, addr = sock.accept()
            print('Cliente Conectado con Socket:', addr)
            thread = Thread(target=capturar_pantalla, args=(conn,))
            thread.start()
    finally:
        sock.close()


if __name__ == '__main__':
    main()
