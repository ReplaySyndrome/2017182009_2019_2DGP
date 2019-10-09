from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global xdir, ydir
    global animation_state
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                if xdir == 0:
                    animation_state = 1
                xdir += 1
            elif event.key == SDLK_LEFT:
                if xdir == 0:
                    animation_state = 0
                xdir -= 1
            elif event.key == SDLK_UP:
                ydir += 1
            elif event.key == SDLK_DOWN:

                ydir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                if xdir != 0:
                    animation_state = 3
                xdir -= 1
            elif event.key == SDLK_LEFT:
                if xdir != 0:
                    animation_state = 2
                xdir += 1
            elif event.key == SDLK_UP:
                ydir -= 1
            elif event.key == SDLK_DOWN:
                ydir += 1




open_canvas()
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
y = 90
frame = 0
xdir = 0
ydir = 0
animation_state = 3

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * animation_state, 100, 100, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8

    x += xdir * 5
    y += ydir * 5
    if x > KPU_WIDTH:
        x = KPU_WIDTH
    if x < 0:
        x = 0

    if y > KPU_HEIGHT:
        y = KPU_HEIGHT
    if y < 0:
        y = 0



close_canvas()

