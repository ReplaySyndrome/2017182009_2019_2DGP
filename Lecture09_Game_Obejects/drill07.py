from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0,400), 90
        self.frame = random.randint(0,7)
        self.image = load_image("run_animation.png")

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Ball:

    def __init__(self):
        temp = random.randint(0,1)
        if temp == 0:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')

        self.x, self.y = random.randint(0, 800), 599
        self.fallSpeed = random.randint(3,8)

    def update(self):
        self.y -= self.fallSpeed

    def draw(self):
        self.image.draw(self.x,self.y)

    pass

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

grass = Grass()
running = True

team = [Boy() for i in range(11)]
balls = [Ball() for i in range(20)]

while running:
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.update()
        boy.draw()

    for ball in balls:
        ball.update()
        ball.draw()
    update_canvas()

    delay(0.05)
    for boy in team:
        if boy.x > 800:
            team.remove(boy)
    print(len(team))
    if len(team) == 0:
        break

# finalization code