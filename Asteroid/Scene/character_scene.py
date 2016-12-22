from pico2d import *
import game_framework
from Object import CPortrait
from Scene import play_scene
from Scene import main_scene

font = None
back_img = None
gauge_img = None
portrait_list = []
player_list = []
selectP1 = 0
selectP2 = 0

def enter():
    global font, back_img, portrait_list, gauge_img
    global selectP1, selectP2
    portrait_list = []

    f = open('game_data.txt', 'r')
    num_player = json.load(f)
    f.close()

    if num_player is 1:
        selectP1 = 0
        selectP2 = -1
    elif num_player is 2:
        selectP1 = 0
        selectP2 = 0

    portrait_list.append(CPortrait.Portrait(get_canvas_width()/2 - 200, get_canvas_height()/2 + 150, 0))
    portrait_list.append(CPortrait.Portrait(get_canvas_width()/2 + 200, get_canvas_height()/2 + 150, 1))

    font = load_font('Resource/font/RPGSystem.ttf', 50)
    back_img = load_image('resource/image/backimg.png')
    gauge_img = load_image('resource/image/gauge.png')
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
            font.draw(
                get_canvas_width() / 2 - 300 + 400 * portrait_list.index(portrait),
                get_canvas_height() / 2,
                'SPEED', (230, 230, 255))
            font.draw(
                get_canvas_width() / 2 - 300 + 400 * portrait_list.index(portrait),
                get_canvas_height() / 2 - 50,
                'ROTATE', (230, 230, 255))
            font.draw(
                get_canvas_width() / 2 - 250 + 400 * portrait_list.index(portrait),
                get_canvas_height() / 2 - 120,
                'SELECT', (230, 230, 255))
            for i in range(0, portrait.speed):
                gauge_img.draw(
                    get_canvas_width() / 2 - 140 + 400 * portrait_list.index(portrait) + 25 * i,
                    get_canvas_height() / 2)
            for i in range(0, portrait.rotate):
                gauge_img.draw(
                    get_canvas_width() / 2 - 140 + 400 * portrait_list.index(portrait) + 25 * i,
                    get_canvas_height() / 2 - 50)
    update_canvas()


def handle_events(frame_time):
    global selectP1, selectP2
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_a:
                selectP1 = clamp(1, selectP1 + 1, 2)
            elif event.key == SDLK_d:
                selectP1 = clamp(1, selectP1 - 1, 2)
            elif event.key == SDLK_LEFT:
                if selectP2 is not -1:
                    selectP2 = clamp(1, selectP2 + 1, 2)
            elif event.key == SDLK_RIGHT:
                if selectP2 is not -1:
                    selectP2 = clamp(1, selectP2 - 1, 2)
        pass


def pause():
    pass


def resume():
    pass
