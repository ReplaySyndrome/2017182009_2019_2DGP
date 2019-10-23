from pico2d import *

import main_state
import game_framework

from pico2d import *

import game_framework
import main_state




name = "MainState"

image = None
grass = None
boy = None
count = 0



class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def enter():
    global pause_image,boy,grass
    pause_image = load_image('pause.png')
    grass = Grass()
    boy = main_state.boy


def exit():
    global pause_image,boy,grass
    del(pause_image)
    del(boy)
    del(grass)


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()
        elif event.type == SDL_QUIT:
            game_framework.quit()


def update():
    global count
    count = count + 1
    if count > 200:
        count = 0


def draw():
    global count

    clear_canvas()
    grass.draw()
    boy.draw()
    if count > 100:
        pause_image.draw(400,300,50,50)

    update_canvas()