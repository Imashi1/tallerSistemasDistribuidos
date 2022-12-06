import customtkinter as ctk
import pygame
from zlib import decompress
import socket
from threading import Thread
from zlib import compress

from mss import mss


# Lado Cliente

def recvall(conn, length):
    buf = b''
    while len(buf) < length:
        data = conn.recv(length - len(buf))
        if not data:
            return data
        buf += data
    return buf


def cliente(ip, puerto):
    pygame.init()
    WIDTH, HEIGHT = 1024, 576

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    watching = True

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip.get(), int(puerto.get())))
    try:
        while watching:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    watching = False
                    break

            # Retreive the size of the pixels length, the pixels length and pixels
            size_len = int.from_bytes(sock.recv(1), byteorder='big')
            size = int.from_bytes(sock.recv(size_len), byteorder='big')
            pixels = decompress(recvall(sock, size))

            # Create the Surface from raw pixels
            img = pygame.image.fromstring(pixels, (1920, 1080), 'RGB')
            img = pygame.transform.scale(img, (WIDTH, HEIGHT))
            # Display the picture
            screen.blit(img, (0, 0))
            pygame.display.flip()
            clock.tick(60)
    finally:
        sock.close()

# Lado servidor


WIDTH = 1920
HEIGHT = 1080


def retreive_screenshot(conn):
    with mss() as sct:
        rect = {'top': 0, 'left': 0, 'width': WIDTH, 'height': HEIGHT}

        while 'recording':
            img = sct.grab(rect)
            pixels = compress(img.rgb, 6)
            size = len(pixels)
            size_len = (size.bit_length() + 7) // 8
            conn.send(bytes([size_len]))
            size_bytes = size.to_bytes(size_len, 'big')
            conn.send(size_bytes)
            conn.sendall(pixels)


def servidor():
    import time
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    serverscreen = ctk.CTkToplevel()
    serverscreen.geometry("400x200")

    label = ctk.CTkLabel(serverscreen, text=("tu ip es " + str(ip)))
    label.pack(side="top", fill="both", expand=True, padx=40, pady=40)
    print(ip)
    time.sleep(3)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, 5555))
    try:
        sock.listen(5)
        while 'connected':
            conn, addr = sock.accept()
            print('Client connected IP:', addr)
            thread = Thread(target=retreive_screenshot, args=(conn,))
            thread.start()
    finally:
        sock.close()


# definimos la apariencia y tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Definimos la pantalla root y su tamanaho
root = ctk.CTk()
root.geometry("500x350")

# Pantalla de inicio
frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(
    master=frame, text="Screen Sharing", text_font=("Roboto", 24))
label.pack(pady=12, padx=10)

botonServer = ctk.CTkButton(
    master=frame, text="Servidor", command=servidor)
botonServer.pack(pady=12, padx=10)

botonHost = ctk.CTkButton(master=frame, text="Cliente")
botonHost.pack(pady=12, padx=10)

# ip = ctk.CTkEntry(master=frame, placeholder_text="Ingresa la IP")
# ip.pack(pady=12, padx=10)

# puerto = ctk.CTkEntry(
#     master=frame, placeholder_text="Ingresa el puerto")
# puerto.pack(pady=12, padx=10)

# button = ctk.CTkButton(master=frame, text="Login",
#                        command=lambda: cliente(ip, puerto))
# button.pack(pady=12, padx=10)


root.mainloop()
