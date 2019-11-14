import random
import json
import os

from pico2d import *
import game_framework
import game_world
import time



name = "MainState"

bird = None

class Bird:
    def __init__(self):
        if bird == None:
            self.image = load_image('bird_animation.png')

        self.dir = 1
        self.velocity = 80
        self.framePerSec = 10
        self.frameX = 0
        self.frameY = 2
        self.currentTime = time.time()
        self.lastTime = time.time()
        self.deltaTime = self.currentTime - self.lastTime

        self.width = 182
        self.height = 167
        self.x = self.width/2
        self.y = 300


    def update(self):
        self.currentTime = time.time()
        self.deltaTime = self.currentTime - self.lastTime
        self.lastTime = self.currentTime
        self.x += self.dir * self.velocity * self.deltaTime
        self.frameX += self.framePerSec * self.deltaTime
        if self.frameY != 0:
            if self.frameX >= 4.99999:
                self.frameX = 0
                self.frameY = self.frameY - 1
        else:
            if self.frameX >= 3.99999:
                self.frameX = 0
                self.frameY = 2

        if self.x > 1600 - self.width/2:
            self.dir = -1
        elif self.x < 0 + self.width/2:
            self.dir = 1


    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(int(self.frameX) * self.width, self.height*self.frameY,
                             self.width, self.height, self.x, self.y)
        else:
            self.image.clip_composite_draw(int(self.frameX) * self.width, self.height*self.frameY,
                             self.width, self.height,0,'h',self.x,self.y,self.width,self.height)






def enter():
    global bird
    bird = Bird()


    game_world.add_object(bird, 0)



def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()



def update():
    for game_object in game_world.all_objects():
        game_object.update()
    # fill here


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
