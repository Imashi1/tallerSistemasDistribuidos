import pygame

width = 700
height = 700
win = pygame.display.set_mode([width, height])

class Jugador():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
pygame.init()

def jugadoresActivos(listaJugador):
    for i in listaJugador:
        i.draw(win)
running = True
#creas el objeto jugador
nJugadores = []
p = Jugador(200,200,10,10,(0,255,0))
p2 = Jugador(200,210,10,10,(0,255,255))
p3 = Jugador(200,220,10,10,(0,255,0))
p4 = Jugador(200,230,10,10,(0,255,255))
p5 = Jugador(200,240,10,10,(0,255,0))
p6 = Jugador(200,250,10,10,(0,255,255))
p7 = Jugador(200,260,10,10,(0,255,0))
p8 = Jugador(200,270,10,10,(0,255,255))
p9 = Jugador(200,280,10,10,(0,255,0))
p10 = Jugador(200,290,10,10,(0,255,255))
p11 = Jugador(200,300,10,10,(0,255,0))
p12 = Jugador(200,330,10,10,(0,255,255))
p13 = Jugador(200,370,10,10,(0,255,0))
p14 = Jugador(200,400,10,10,(0,255,255))

nJugadores.append(p)
nJugadores.append(p2)
nJugadores.append(p3)
nJugadores.append(p4)
nJugadores.append(p5)
nJugadores.append(p6)
nJugadores.append(p7)
nJugadores.append(p8)
nJugadores.append(p9)
reloj = pygame.time.Clock()

while running:
    
    reloj.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    win.fill((255,255,255))
    jugadoresActivos(nJugadores)
    #ejecuta metodo moverse
    for i in nJugadores:
        i.move()
    
    #redibuja el movimiento nuevo
    
    
    pygame.display.flip()
pygame.quit()
