from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_MOUSEBUTTONDOWN:
            pass


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')


running = True
x = 800 // 2
y = 90
frame = 0
to_x = 800//2
to_y = 90
animation_state = 3

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * animation_state, 100, 100, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8





close_canvas()