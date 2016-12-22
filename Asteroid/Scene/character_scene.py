from pico2d import *
import game_framework
from Object import CPortrait
from Scene import play_scene
from Scene import main_scene

font = None
back_img = None
portrait_list = []

def enter():
    global font, back_img, portrait_list
    portrait_list = []

    portrait_list.append(CPortrait.Portrait(get_canvas_width()/2 - 300, get_canvas_height()/2 + 100, 0))
    portrait_list.append(CPortrait.Portrait(get_canvas_width()/2 + 300, get_canvas_height()/2 + 100, 1))

    font = load_font('Resource/font/RPGSystem.ttf', 50)
    back_img = load_image('resource/image/backimg.png')
    pass


def exit():
    pass


def update(frame_time):
    pass


def draw():
    clear_canvas()
    back_img.draw(get_canvas_width()/2, get_canvas_height()/2)
    if len(portrait_list) is not 0:
        for portrait in portrait_list:
            portrait.draw()

    update_canvas()


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
        pass


def pause():
    pass


def resume():
    pass
