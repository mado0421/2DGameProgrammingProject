import platform
import os
if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"

import game_framework
import pico2d
from states import main_state

pico2d.open_canvas(1280, 800, sync=True)
game_framework.run(main_state)
pico2d.close_canvas()
