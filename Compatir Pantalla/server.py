import socket
from threading import Thread
from zlib import compress

from mss import mss

WIDTH = 1920
HEIGHT = 1080

def retreive_screenshot(conn):
    with mss() as sct:
        # The region to capture
        rect = {'top': 0, 'left': 0, 'width': WIDTH, 'height': HEIGHT}

        while 'recording':
            # carptura el screen
            img = sct.grab(rect)
            # Ajusta la  compresión (0-9)
            pixels = compress(img.rgb, 6)

            # Envia el tamañ la longitud de píxeles
            size = len(pixels)
            size_len = (size.bit_length() + 7) // 8
            conn.send(bytes([size_len]))

            # Envia la logintud actual
            size_bytes = size.to_bytes(size_len, 'big')
            conn.send(size_bytes)

            # Envia los pixeles
            conn.sendall(pixels)

def main():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("192.168.1.92", 5555))
    try:
        sock.listen(5)
        print('Server started.')

        while 'connected':
            conn, addr = sock.accept()
            print('Client connected IP:', addr)
            thread = Thread(target=retreive_screenshot, args=(conn,))
            thread.start()
    finally:
        sock.close()


if __name__ == '__main__':
    main()
