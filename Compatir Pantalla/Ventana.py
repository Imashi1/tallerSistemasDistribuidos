import customtkinter
import customtkinter as ctk
import pygame
from zlib import decompress
import socket

ANCHO, ALTO = 1024, 576


def recvall(conn, length):
    buf = b''
    while len(buf) < length:
        data = conn.recv(length - len(buf))
        if not data:
            return data
        buf += data
    return buf


def verPantalla(ip, puerto):
    pygame.init()

    screen = pygame.display.set_mode((ANCHO, ALTO))
    clock = pygame.time.Clock()
    running = True

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip.get(), int(puerto.get())))
    try:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break

<<<<<<< Updated upstream
            # El tamaño de la longitud de píxeles, la longitud de los píxeles y los píxeles
=======
            # Captura los pixeles
>>>>>>> Stashed changes
            size_len = int.from_bytes(sock.recv(1), byteorder='big')
            size = int.from_bytes(sock.recv(size_len), byteorder='big')
            pixels = decompress(recvall(sock, size))

<<<<<<< Updated upstream
            # Crear la superficie a partir de píxeles en bruto
            img = pygame.image.fromstring(pixels, (1920, 1080), 'RGB')
            img = pygame.transform.scale(img, (WIDTH, HEIGHT))
            # Muestra el screen
=======
            # Crea la Superficie para depositar los pixeles capturados
            img = pygame.image.fromstring(pixels, (1920, 1080), 'RGB')

            #Reescala la imagen parase aprecie de mejor forma
            img = pygame.transform.scale(img, (ANCHO, ALTO))
            
            # Muestra la imagen
>>>>>>> Stashed changes
            screen.blit(img, (0, 0))
            pygame.display.flip()
            clock.tick(60)
    finally:
        sock.close()
        pygame.quit()
        root.destroy()


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
    master=frame, text="Screen Sharing", font=("Roboto", 24))
label.pack(pady=12, padx=10)

ip = ctk.CTkEntry(master=frame, placeholder_text="Ingresa la IP")
ip.pack(pady=12, padx=10)

puerto = ctk.CTkEntry(
    master=frame, placeholder_text="Ingresa el puerto")
puerto.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text="Entrar",
                       command=lambda: verPantalla(ip, puerto))
button.pack(pady=12, padx=10)


root.mainloop()
