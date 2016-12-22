from pico2d import *
import game_framework
from Scene import main_scene

back_img = None
font = None

def enter():
    global back_img, font
    font = load_font('resource/font/RPGSystem.ttf', 50)
    back_img = load_image('resource/image/backimg.png')
    pass

def bubble_sort(data):
    for i in range(0, len(data)):
        for j in range(i+1, len(data)):
            if data[i]['Score'] < data[j]['Score']:
                data[i], data[j] = data[j], data[i]

def draw_ranking():

    font.draw(get_canvas_width()/2 - 90, get_canvas_height()/2 + 290, '[RANKING]', (230, 230, 255))

    f = open('data_score_file.txt', 'r')
    score_data = json.load(f)
    f.close()

    bubble_sort(score_data)

    score_data = score_data[:10]

    font.draw(get_canvas_width()/2 - 90 + 200, get_canvas_height()/2 + 250, '[SCORE]', (230, 230, 255))
    y = 0
    for score in score_data:
        font.draw(get_canvas_width()/2 - 100 + 200, 200 + get_canvas_height()/2 - 40 * y,
                  'SCORE:%5.1d' % score['Score'],
                  (190, 190, 205))
        y += 1

    f = open('data_time_file.txt', 'r')
    score_data = json.load(f)
    f.close()

    bubble_sort(score_data)

    score_data = score_data[:10]

    font.draw(get_canvas_width()/2 - 90 - 200, get_canvas_height()/2 + 250, '[TIME]', (230, 230, 255))
    y = 0
    for score in score_data:
        font.draw(get_canvas_width()/2 - 100 - 200, 200 + get_canvas_height()/2 - 40 * y,
                  'Time:%5.1f' % score['Score'],
                  (190, 190, 205))
        y += 1

def exit():
    pass


def update(frame_time):
    pass


def draw():
    clear_canvas()
    back_img.draw(get_canvas_width()/2, get_canvas_height()/2)
    draw_ranking()
    update_canvas()


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            print(frame_time)
            game_framework.change_state(main_scene)


def pause():
    pass


def resume():
    pass
