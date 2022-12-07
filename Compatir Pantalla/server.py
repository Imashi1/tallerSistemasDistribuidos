import socket
from threading import Thread
from zlib import compress

from mss import mss

WIDTH = 1920
HEIGHT = 1080

<<<<<<< Updated upstream
def retreive_screenshot(conn):
=======


def capturar_pantallazo(conn):
    #Captura de pantallazos continuos
>>>>>>> Stashed changes
    with mss() as sct:
        #Región a tomar capturas
        rect = {'top': 0, 'left': 0, 'width': WIDTH, 'height': HEIGHT}

        while 'recording':
<<<<<<< Updated upstream
            # carptura el screen
            img = sct.grab(rect)
            # Ajusta la  compresión (0-9)
            pixels = compress(img.rgb, 6)

            # Envia el tamañ la longitud de píxeles
=======
            #Compresión de imagenes
            img = sct.grab(rect)
            pixels = compress(img.rgb, 6)

>>>>>>> Stashed changes
            size = len(pixels)
            size_len = (size.bit_length() + 7) // 8
            #Envía largo de pixeles
            conn.send(bytes([size_len]))

<<<<<<< Updated upstream
            # Envia la logintud actual
            size_bytes = size.to_bytes(size_len, 'big')
            conn.send(size_bytes)

            # Envia los pixeles
=======
            #Envía tamaño bytes
            size_bytes = size.to_bytes(size_len, 'big')
            conn.send(size_bytes)

>>>>>>> Stashed changes
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
            thread = Thread(target=capturar_pantallazo, args=(conn,))
            thread.start()
    finally:
        sock.close()


if __name__ == '__main__':
    main()
