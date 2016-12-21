from pico2d import *


def enter():
    pass


def exit():
    pass


def update(frame_time):
    print(frame_time)
    pass


def draw():
    clear_canvas()
    update_canvas()


def handle_events(frame_time):
    events = get_events()
    for event in events:
        pass


def pause():
    pass


def resume():
    pass
