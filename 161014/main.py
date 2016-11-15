import game_framework
import pico2d
from states import test_state
from states import main_state
from states import ranking_state
from states import charSelc_state

pico2d.open_canvas(1280, 800, sync=True)
game_framework.run(main_state)
pico2d.close_canvas()
