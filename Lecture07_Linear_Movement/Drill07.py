from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_MOUSEBUTTONDOWN:
            to_x, to_y = event.x, KPU_HEIGHT -1 - event.y


def go_to_destination(p1,p2):
    global frame
    global x, y
    for i in range(0, 100 + 1, 2):
        clear_canvas()
        kpu_ground.draw(1280//2,1024//2)
        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)

    Move = False




open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')


running = True
x = 800 // 2
y = 90
frame = 0
to_x = 800
to_y = 600
animation_state = 3

Move = True

while running:
    if Move == True:
        go_to_destination((x, y), (to_x, to_y))
    else:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)





close_canvas()