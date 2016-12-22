import platform
import os
if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"

import game_framework
import pico2d
from Scene import play_scene
from Scene import character_scene
from Scene import main_scene

pico2d.open_canvas(1280, 720)
game_framework.run(main_scene)
pico2d.close_canvas()
