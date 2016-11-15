import game_framework
from pico2d import *
from states import main_state

name = "RankingState"
image = None
font = None


def enter():
    global image
    image = load_image('resource/image/back_gamestate.png')
    global font
    font = load_font('resource/font/RPGSystem.ttf', 50)


def exit():
    global image, font
    del(image)
    del(font)


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(main_state)


def update(frame_time):
    pass


def bubble_sort(data):
    for i in range(0, len(data)):
        for j in range(i+1, len(data)):
            if data[i]['Score'] < data[j]['Score']:
                data[i], data[j] = data[j], data[i]


def draw_ranking():

    f = open('data_file.txt', 'r')
    score_data = json.load(f)
    f.close()

    bubble_sort(score_data)

    score_data = score_data[:10]

    font.draw(get_canvas_width()/2 - 90, get_canvas_height()/2 + 200, '[RANKING]', (255, 255, 255))
    y = 0
    for score in score_data:
        font.draw(get_canvas_width()/2 - 100, 100 + get_canvas_height()/2 - 40 * y,
                  'SCORE:%5.1d' % score['Score'],
                  (255, 255, 255))
        y += 1


def draw():
    global image, font
    clear_canvas()
    image.draw(get_canvas_width()/2, get_canvas_height()/2)
    draw_ranking()
    update_canvas()
