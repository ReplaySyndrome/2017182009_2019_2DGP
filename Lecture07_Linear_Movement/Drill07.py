from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global x,y
    global to_x, to_y
    global move
    global movedirection
    global i
    global mousex,mousey
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_MOUSEBUTTONDOWN:
            to_x, to_y = event.x, KPU_HEIGHT - 1 - event.y
            if to_x > x:
                movedirection = 1
            else:
                movedirection = 0
            i=0
            move = True
        if event.type == SDL_MOUSEMOTION:
            mousex, mousey = event.x, KPU_HEIGHT - 1 - event.y









open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hide_cursor()
handArrow = load_image("hand_arrow.png")


running = True
x = 800 // 2
y = 90
frame = 0
to_x = 800
to_y = 600
animation_state = 3
movedirection = 1
i = 1000
move = False
mousex = 0
mousey = 0

while running:
    if move:
        while i < 1000:
            clear_canvas()
            kpu_ground.draw(1280 // 2, 1024 // 2)
            t = i / 1000
            x = (1 - t) * x + t * to_x
            y = (1 - t) * y + t * to_y
            character.clip_draw(frame * 100, 100 * movedirection, 100, 100, x, y)
            handArrow.draw(mousex + 20, mousey - 20)
            update_canvas()
            frame = (frame + 1) % 8
            handle_events()
            i += 1

            delay(0.05)
        move = False
    else:
        clear_canvas()
        kpu_ground.draw(1280 // 2, 1024 // 2)
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        handArrow.draw(mousex + 20, mousey - 20)
        update_canvas()
        frame = (frame + 1) % 8

        delay(0.05)
    handle_events()





close_canvas()