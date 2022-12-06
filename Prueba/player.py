import pygame as pg
import math
POS_START = (192, 160)


class Player(object):

    def __init__(self, game, x, y, color):
        self.game = game
        self.x = x
        self.y = y
        self.color = color
        self.rect = pg.Rect(x, y, 16, 16)

    def draw(self):
        pg.draw.rect(self.game.win, self.color, self.rect)

    def update(self):
        self.movement()
        self.endmap()

    def move(self, dx, dy):
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):

        # Move the rect
        self.rect.x += dx // 2
        self.rect.y += dy // 2

        # If you collide with a wall, move out based on velocity
        for wall in self.game.walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

    def movement(self):
        key = pg.key.get_pressed()
        if key[pg.K_LEFT]:
            self.move(-2, 0)
        if key[pg.K_RIGHT]:
            self.move(2, 0)
        if key[pg.K_UP]:
            self.move(0, -2)
        if key[pg.K_DOWN]:
            self.move(0, 2)

    def endmap(self):
        if self.rect.x == 416:
            self.rect = pg.Rect(0, 160, 16, 16)
            pg.draw.rect(self.game.win, self.color, self.rect)
        if self.rect.x == -16:
            self.rect = pg.Rect(416, 160, 16, 16)
            pg.draw.rect(self.game.win, self.color, self.rect)

# class Power(object):
#     def __init__(self, x, y, color):
#         self.x = x
#         self.y = y
#         self.color = color
#         self.rect = pg.Rect(x, y, 16, 16)

#     def devolverJugador(self, blueTeam, redTeam):
#         redPlayer = random.choice(blueTeam)
#         redPlayer.rect = pg.Rect(192, 272, 16, 16)
#         pg.draw.rect(win, 'blue', redPlayer.rect)
#         redTeam.remove(redTeam)
#         blueTeam.append(redPlayer)
