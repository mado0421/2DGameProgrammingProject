from pico2d import *
import game_framework
from Scene import play_scene

num_player = None

def enter():
    global num_player
    num_player = 0
    pass


def exit():
    f = open('game_data.txt', 'w')
    json.dump(num_player, f)
    f.close()
    pass


def update(frame_time):
    print(frame_time)
    pass


def draw():
    clear_canvas()
    update_canvas()


def handle_events(frame_time):
    global num_player
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:
                num_player = 1
            elif event.key == SDLK_s:
                num_player = 2
            game_framework.change_state(play_scene)


def pause():
    pass


def resume():
    pass
