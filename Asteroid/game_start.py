import game_framework
import pico2d
from Scene import main_scene

pico2d.open_canvas(1280, 720)
game_framework.run(main_scene)
pico2d.close_canvas()
