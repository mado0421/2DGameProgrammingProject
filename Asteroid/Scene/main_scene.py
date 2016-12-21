from pico2d import *
import game_framework
from Object import CAsteroid

asteroid = []
time = None

def enter():
    global time
    time = 0
    pass


def exit():
    pass


def update(frame_time):
    global time
    if (time + frame_time) > 1:
        print(time)
    time = (time + frame_time) % 1.0
    # print(time)

    # print(frame_time)
    pass


def draw():
    clear_canvas()
    update_canvas()


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type is SDL_QUIT:
            game_framework.quit()
        elif event.type is SDL_KEYDOWN and event.key is SDLK_ESCAPE:
            print(frame_time)
            game_framework.quit()
        else:
            pass


def pause():
    pass


def resume():
    pass
