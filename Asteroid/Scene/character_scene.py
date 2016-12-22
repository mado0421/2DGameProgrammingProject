from pico2d import *
import game_framework
from Scene import play_scene
from Scene import main_scene

font = None


def enter():
    global font
    font = load_font('Resource/font/RPGSystem.ttf', 50)
    pass


def exit():
    pass


def update(frame_time):
    pass


def draw():
    clear_canvas()
    font.draw(get_canvas_width()/2 - 90, get_canvas_height()/2 + 110, 'LOCAL SINGLE PLAY', (230, 230, 255))
    font.draw(get_canvas_width()/2 - 90, get_canvas_height()/2 + 210, 'LOCAL MULTI PLAY', (230, 230, 255))

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
