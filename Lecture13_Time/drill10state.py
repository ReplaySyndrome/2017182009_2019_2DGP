import random
import json
import os

from pico2d import *
import game_framework
import game_world
import time

from boy import Boy
from grass import Grass


name = "MainState"

boy = None
bird = None

class Bird:
    def __init__(self):
        if bird == None:
            self.image = load_image('bird_animation.png')

        self.dir = 1
        self.velocity = 30
        self.framePerSec = 10
        self.frameX = 0
        self.frameY = 0
        self.currentTime = time.time()
        self.lastTime = time.time()
        self.deltaTime = self.currentTime - self.lastTime
        self.x = 0
        self.y = 300


    def update(self):
        self.currentTime = time.time()
        self.deltaTime = self.currentTime - self.lastTime
        self.lastTime = self.currentTime
        self.x += self.dir * self.velocity * self.deltaTime
        

    def draw(self):
        self.image.clip_draw(0,168,183,168,self.x,self.y)



def enter():
    global boy,bird
    bird = Bird()
    boy = Boy()
    grass = Grass()

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
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    # fill here


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()