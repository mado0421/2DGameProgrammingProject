from pico2d import *
import game_framework
from states import game_state
from classes import CButton

name = "MainState"
back_image = None
button_list = []


def enter():
    global back_image, button_list
    button_list.append(CButton.Button('start', get_canvas_width()/2, get_canvas_height()/2 - 100, 'start'))
    button_list.append(CButton.Button('option', get_canvas_width()/2, get_canvas_height()/2 - 150, 'game'))
    button_list.append(CButton.Button('rank', get_canvas_width()/2, get_canvas_height()/2 - 200, 'game'))
    button_list.append(CButton.Button('quit', get_canvas_width()/2, get_canvas_height()/2 - 250, 'game'))
    back_image = load_image('resource/image/back_gamestate.png')


def exit():
    global button_list
    del(button_list)
    pass

def update(frame_time):
    delay(0.01)


def draw():
    clear_canvas()
    back_image.draw(get_canvas_width()/2, get_canvas_height()/2)
    for button in button_list:
        button.draw()
    update_canvas()


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_MOUSEBUTTONDOWN:
            for button in button_list:
                if button.is_on(event.x, get_canvas_height() - event.y):
                    if button.tag is 'start':
                        game_framework.push_state(game_state)
        else:
            for button in button_list:
                button.handle_event(event)


def pause():
    pass


def resume():
    pass
