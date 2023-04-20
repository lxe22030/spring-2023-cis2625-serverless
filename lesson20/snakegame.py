import pygame as pg
from game_objects import *
import sys

#basic game methods
class Game:
    def __init__(self):
        pg.init()
        self.WINDOW_SIZE = 1000
        self.screen = pg.display.setmode([self.WINDOW_SIZE] * 2)
        self.clock = pg.time.Clock()
    
    def new_game(self):
        pass
    
    def update(self):
        pg.display.flip()
        #60 frames per second
        self.clock.tick(60)
    
    def draw(self):
        #makes the drawing surface black
        self.screen.fill('black')
    
    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
    
    def run(self):
        self.check_event()
        self.update()
        self.draw()
    
if __name__ =='__main__':
    game = Game()
    game.run()
    