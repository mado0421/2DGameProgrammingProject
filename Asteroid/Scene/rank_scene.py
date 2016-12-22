from pico2d import *
import game_framework

back_img = None


def enter():
    global back_img
    back_img = load_image('resource/image/backimg.png')
    pass


def exit():
    pass


def update(frame_time):
    print(frame_time)
    pass


def draw():
    clear_canvas()
    back_img.draw(get_canvas_width()/2, get_canvas_height()/2)
    update_canvas()


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            print(frame_time)
            game_framework.quit()


def pause():
    pass


def resume():
    pass
