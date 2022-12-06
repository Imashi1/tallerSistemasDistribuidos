import pygame as pg
import sys
import os
from constantes import *
from player import *
from map import *
from network import *
os.environ["SDL_VIDEO_CENTERED"] = "1"


class Game:
    def __init__(self):
        pg.init()
        self.win = pg.display.set_mode((416, 368))
        self.clock = pg.time.Clock()
        self.walls = []
        self.new_game()

    def new_game(self):
        x = y = 0
        for row in level:
            for col in row:
                if col == "W":
                    self.map = Map(self, (x, y))
                x += 16
            y += 16
            x = 0
        self.n = Network()
        p = self.n.getP()
        print(p)
        # self.player = Player(self, 192, 160, 'red')
        # self.player2 = Player(self, 192, 272, 'blue')

    def update(self):
        # self.player.update()
        # self.player2.update()
        self.clock.tick(60)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.map.draw()
        # self.player.draw()
        # self.player2.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                print("Juego Cerrado")
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
            pg.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run()
