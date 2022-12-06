import pygame as pg

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


class Map:

    def __init__(self, game, pos):
        self.game = game
        self.mini_map = level
        self.rect = pg.Rect(pos[0], pos[1], 16, 16)
        game.walls.append(self)

    def draw(self):
        for wall in self.game.walls:
            pg.draw.rect(self.game.win, (255, 255, 255), wall.rect)
