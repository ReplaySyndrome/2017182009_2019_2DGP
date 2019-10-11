from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


#total commit time is 7





open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')




running = True
x = 800 // 2
y = 90
frame = 0
size = 10
points = [(random.randint(-500, 500), random.randint(-350, 350)) for i in range(size)]

print(points)

while running:
    clear_canvas()
    kpu_ground.draw(1280 // 2, 1024 // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)





close_canvas()