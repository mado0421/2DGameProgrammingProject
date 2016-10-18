from pico2d import *
import select_state

name = "MainState"
back_image = None
canvas_width = 1280
canvas_height = 800


def enter():
    global back_image
    open_canvas(canvas_width, canvas_height, sync=True)
    back_image = load_image('resource/image/back_gamestate.png')


def exit():
    close_canvas()


def update():
    delay(0.01)


def draw():
    clear_canvas()
    update_canvas()


def handle_events():
    events = get_events()


def pause():
    pass


def resume():
    pass
