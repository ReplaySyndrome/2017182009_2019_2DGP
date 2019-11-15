from pico2d import *
import game_framework
import time
class Movingground:
    def __init__(self):
        self.image = load_image('brick180x40.png')
        self.x = 90
        self.y = 200
        self.dir = 1
        self.speed = 200
        self.currTime = None
        self.lastTime = time.time()
        self.deltaTime = None

    def update(self):

        if self.x > 1600 - 90:
            self.dir = -1
        elif self.x < 90:
            self.dir = 1
        self.x += self.dir *self.speed * game_framework.frame_time
        print(game_framework.frame_time)

    def draw(self):
        self.image.draw(self.x,self.y)
        draw_rectangle(*self.get_bb())



    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20