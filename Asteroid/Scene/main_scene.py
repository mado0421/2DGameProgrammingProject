from pico2d import *
import game_framework
from Scene import play_scene
from Scene import rank_scene
from Scene import option_scene
from Scene import character_scene

num_player = None
font = None
back_img = None
highlight_img = None
select_img = None
select = 0

def enter():
    global font, back_img, highlight_img, select_img
    font = load_font('Resource/font/RPGSystem.ttf', 50)
    back_img = load_image('Resource/image/backimg.png')
    highlight_img = load_image('Resource/image/highlight.png')
    select_img = load_image('Resource/image/selectimg.png')
    global num_player, select
    num_player = 0
    select = 0
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
    back_img.draw(get_canvas_width()/2, get_canvas_height()/2)
    font.draw(get_canvas_width()/2 - 400, get_canvas_height()/2 - 50, 'LOCAL SINGLE PLAY', (200, 200, 255))
    font.draw(get_canvas_width()/2 - 400, get_canvas_height()/2 - 100, 'LOCAL MULTI PLAY', (200, 200, 255))
    font.draw(get_canvas_width()/2 - 400, get_canvas_height()/2 - 150, 'OPTION', (200, 200, 255))
    font.draw(get_canvas_width()/2 - 400, get_canvas_height()/2 - 200, 'RANK', (200, 200, 255))
    font.draw(get_canvas_width()/2 - 400, get_canvas_height()/2 - 250, 'QUIT', (200, 200, 255))

    if select is not 0:
        highlight_img.draw(get_canvas_width() / 2 - 200, get_canvas_height()/2 - 50 * select)
        select_img.draw(get_canvas_width() / 2 - 450, get_canvas_height() / 2 - 50 * select)
    update_canvas()


def handle_events(frame_time):
    global num_player, select
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_DOWN:
                select = clamp(1, select + 1, 5)
            elif event.key == SDLK_UP:
                select = clamp(1, select - 1, 5)
            elif event.key == SDLK_RETURN:
                if select is 1:
                    num_player = 1
                    game_framework.change_state(play_scene)
                elif select is 2:
                    num_player = 2
                    game_framework.change_state(character_scene)
                elif select is 3:
                    game_framework.change_state(option_scene)
                elif select is 4:
                    game_framework.change_state(rank_scene)
                elif select is 5:
                    game_framework.quit()
            if event.key == SDLK_ESCAPE:
                game_framework.quit()


def pause():
    pass


def resume():
    pass
