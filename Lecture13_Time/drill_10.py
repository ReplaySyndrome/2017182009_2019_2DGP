import game_framework
import pico2d

import drill10state

pico2d.open_canvas(1600, 600)
game_framework.run(drill10state)
pico2d.close_canvas()