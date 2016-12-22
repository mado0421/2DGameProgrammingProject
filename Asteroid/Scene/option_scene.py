from pico2d import *
import game_framework

font = None
back_img = None

def enter():
    global font, back_img
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
