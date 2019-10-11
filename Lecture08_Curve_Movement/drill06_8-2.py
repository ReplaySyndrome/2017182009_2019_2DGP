from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
y = 90
frame = 0
size = 10
points = [(random.randint(0, 1280), random.randint(0, 1024)) for i in range(size)]

def character_move(p1,p2,p3,p4):
    global frame
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2
        clear_canvas()
        kpu_ground.draw(1280 // 2, 1024 // 2)
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)


while running:
    character_move(points[9],points[0],points[1],points[2])
    character_move(points[0], points[1], points[2], points[3])
    character_move(points[1], points[2], points[3], points[4])
    character_move(points[2], points[3], points[4], points[5])
    character_move(points[3],points[4], points[5], points[6])
    character_move(points[4], points[5], points[6], points[7])
    character_move(points[5],points[6], points[7], points[8])
    character_move(points[6], points[7], points[8], points[9])
    character_move(points[7], points[8], points[9], points[0])
    character_move(points[8], points[9], points[0], points[1])




close_canvas()