import game_framework
import pico2d
from states import test_state

pico2d.open_canvas()
game_framework.run(test_state)
pico2d.close_canvas()
