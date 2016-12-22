from pico2d import *
import game_framework
from Object import CPlane
from Object import CPlayer
from Object import CAsteroid
from Object import CBullet


player_list = []
bullet_list = []
asteroid_list = []
plane_list = []
time = None
font = None
asteroid_timer = None
plane_timer = None


def enter():
    global font
    global time, asteroid_timer, plane_timer
    global asteroid_list, plane_list, player_list, bullet_list
    player_list = []
    bullet_list = []
    asteroid_list = []
    plane_list = []
    time = 0
    asteroid_timer = 0
    plane_timer = 0
    font = load_font('Resource/font/RPGSystem.ttf', 50)

    f = open('game_data.txt', 'r')
    num_player = json.load(f)
    f.close()

    if num_player is 1:
        player_list.append(CPlayer.Player(0, 0))
    elif num_player is 2:
        player_list.append(CPlayer.Player(1, 0))
        player_list.append(CPlayer.Player(2, 1))
    print(num_player)

    pass


def exit():
    global asteroid_list, plane_list
    pass


def update(frame_time):
    global time, asteroid_timer, plane_timer
    global asteroid_list, plane_list
    time += frame_time
    asteroid_timer += frame_time
    plane_timer += frame_time

    if asteroid_timer > 1.0:
        asteroid_timer = 0
        asteroid_list.append(CAsteroid.Asteroid())

    if plane_timer > 1.5:
        plane_timer = 0
        plane_list.append(CPlane.Plane())

    if len(player_list) is not 0:
        for player in player_list:
            player.update(frame_time)

    if len(asteroid_list) is not 0:
        for asteroid in asteroid_list:
            asteroid.update(frame_time)
            if asteroid.check_out():
                asteroid_list.remove(asteroid)

    if len(plane_list) is not 0:
        for plane in plane_list:
            plane.update(frame_time)
            if plane.check_out() or plane.check_dead():
                plane_list.remove(plane)

    pass


def draw():
    clear_canvas()

    font.draw(get_canvas_width()/2 - 90, get_canvas_height()/2 + 290, 'Plane: %5.1d' % len(plane_list), (230, 230, 255))

    if len(player_list) is not 0:
        for player in player_list:
            player.draw()

    if len(asteroid_list) is not 0:
        for asteroid in asteroid_list:
            asteroid.draw()

    if len(plane_list) is not 0:
        for plane in plane_list:
            plane.draw()

    update_canvas()


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            print(frame_time)
            game_framework.quit()
        else:
            if len(player_list) is not 0:
                for player in player_list:
                    player.handle_events(event)


def pause():
    pass


def resume():
    pass
