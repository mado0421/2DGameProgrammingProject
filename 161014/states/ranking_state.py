import game_framework
from pico2d import *
from classes import CButton
from states import main_state

name = "RankingState"
image = None
font = None
button_list = None

def enter():
    global image, button_list, font
    button_list = []
    button_list.append(CButton.Button('back', get_canvas_width()/2, get_canvas_height()/2 - 250, 'main'))
    image = load_image('resource/image/back_gamestate.png')
    font = load_font('resource/font/RPGSystem.ttf', 50)


def exit():
    global image, font, button_list
    del(image)
    del(font)
    del(button_list)


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_MOUSEBUTTONDOWN:
            for button in button_list:
                if button.is_on(event.x, get_canvas_height() - event.y):
                    if button.tag is 'main':
                        game_framework.push_state(main_state)
        else:
            for button in button_list:
                button.handle_event(event)


def update(frame_time):
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


def draw():
    global image, font, button_list
    clear_canvas()
    image.draw(get_canvas_width()/2, get_canvas_height()/2)
    draw_ranking()
    for button in button_list:
        button.draw()
    update_canvas()
