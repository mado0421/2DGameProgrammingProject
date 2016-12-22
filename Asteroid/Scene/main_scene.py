from pico2d import *
import game_framework
from Scene import play_scene

num_player = None
font = None


def enter():
    global font
    font = load_font('Resource/font/RPGSystem.ttf', 50)

    global num_player
    num_player = 0
    pass


def exit():
    f = open('game_data.txt', 'w')
    json.dump(num_player, f)
    f.close()
    pass


def update(frame_time):
    pass


def draw():
    clear_canvas()
    font.draw(get_canvas_width()/2 - 90, get_canvas_height()/2 + 110, 'LOCAL SINGLE PLAY', (230, 230, 255))
    font.draw(get_canvas_width()/2 - 90, get_canvas_height()/2 + 210, 'LOCAL MULTI PLAY', (230, 230, 255))

    update_canvas()


def handle_events(frame_time):
    global num_player
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:
                num_player = 1
                game_framework.change_state(play_scene)
            elif event.key == SDLK_s:
                num_player = 2
                game_framework.change_state(play_scene)
            if event.key == SDLK_ESCAPE:
                game_framework.quit()


def pause():
    pass


def resume():
    pass
