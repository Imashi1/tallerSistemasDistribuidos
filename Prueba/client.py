from network import Network
from player import Player
import os
import pygame
import random
import numpy as np
# Class for the orange dude

# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

# Set up the display
pygame.display.set_caption("Pilladas")
win = pygame.display.set_mode((416, 368))


# Nice class to hold a wall rect


# class Power(object):
#     def __init__(self, x, y, color):
#         self.x = x
#         self.y = y
#         self.color = color
#         self.rect = pygame.Rect(x, y, 16, 16)

#     def devolverJugador(self, blueTeam, redTeam):
#         redPlayer = random.choice(blueTeam)
#         redPlayer.rect = pygame.Rect(192, 272, 16, 16)
#         pygame.draw.rect(win, 'blue', redPlayer.rect)
#         redTeam.remove(redTeam)
#         blueTeam.append(redPlayer)


class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)


walls = []  # List to hold the walls
POS_START = (192, 160)
level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWW",
    "WE          W           EW",
    "W WWW WWWW  W  WWWW WWWW W",
    "W WWW WWWW  W  WWWW WWWW W",
    "W                        W",
    "W WWW  W WWWWWWW W   WWW W",
    "W      W    W    W       W",
    "WWWWWW WWW  W  WWW WWWWWWW",
    "WWWWWW W         W WWWWWWW",
    "WWWWWW W WWW WWW W WWWWWWW",
    "         W     W          ",
    "WWWWWW W WWWWWWW W WWWWWWW",
    "WWWWWW W         W WWWWWWW",
    "W      W WWWWWWW         W",
    "W WWW  W    W        WWW W",
    "W   W       W        W   W",
    "WWW W WWWWW W WWWWWW W WWW",
    "W                        W",
    "WWW  W  WWWWWWWWWW W W WWW",
    "W    W      W      W     W",
    "W WWWWWWW  WWW  WWWWWWWW W",
    "WE                      EW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWW",
]

pillado = pygame.USEREVENT + 0


pygame.time.set_timer(pillado, 0)

clock = pygame.time.Clock()
walls = []  # List to hold the walls
# player = Player() # Create the player

# Holds the level layout in a list of strings.


# Parse the level string above. W = wall, E = exit
x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16
    x = 0

n = Network()
p = n.getP()
player = Player(win, 192, 160, 'red')  # CENTRO
player2 = Player(win, 192, 272, 'blue')
player3 = Player(win, 192, 336, 'blue')
player4 = Player(win, 16, 32, 'blue')
# power = Power(32, 160, (255, 182, 120))
blueTeam = [player2, player3, player4]
redTeam = [player]
running = True
while running:

    # print(posInicial)
    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
        # if e.type == pillado:
        #     # player.collision(bluePlayer, blueTeam)
        #     print(bluePlayer.__dict__)
        #     pygame.time.set_timer(pillado, 0)

    # power.rect.x = powerPos[0]
    # power.rect.y = powerPos[1]

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0, walls)
        # print(player.rect.x)
    if key[pygame.K_RIGHT]:
        player.move(2, 0, walls)
    if key[pygame.K_UP]:
        player.move(0, -2, walls)
    if key[pygame.K_DOWN]:
        player.move(0, 2, walls)

    # Just added this to make it slightly fun ;)
    if len(blueTeam) == 0:
        raise SystemExit("You win!")

    for bluePlayer in blueTeam:
        if player.rect.colliderect(bluePlayer):
            setattr(bluePlayer, "color", 'red')
            player.collision(win, bluePlayer, blueTeam, redTeam)
    # for bluePlayer in blueTeam:
    #     if bluePlayer.rect.colliderect(power):
    #         power.devolverJugador(blueTeam, redTeam)
        # print(bluePlayer.__dict__)
        # pygame.time.set_timer(pillado, 30)
    # Draw the scene
    win.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(win, 'skyblue', wall.rect)
    pygame.draw.rect(win, player.color, player.rect)
    pygame.draw.rect(win, player2.color, player2.rect)
    pygame.draw.rect(win, player3.color, player3.rect)
    pygame.draw.rect(win, player4.color, player4.rect)
    # pygame.draw.rect(win, (255, 182, 120), power.rect)
    player.update()
    pygame.display.flip()
