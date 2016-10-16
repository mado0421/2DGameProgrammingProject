from pico2d import *
from Cplayer import *
import CBullet
import Cparticle
import game_framework

name = "GameState"
player = None
back_image = None
bullet_list = []
particle_list = []
canvas_width = 1280
canvas_height = 800


def enter():
    global player
    global back_image
    open_canvas(canvas_width, canvas_height)
    back_image = load_image('resource/image/back_gamestate.png')
    player = Player(1)


def exit():
    global player
    global bullet_list
    global particle_list
    del(player)
    del(bullet_list)
    del(particle_list)
    close_canvas()


def update():
    player.update()
    particle_list.append(Cparticle.Particle(player.nozzle_x, player.nozzle_y, 10))
    if bullet_list.count is not 0:
        for bullet in bullet_list:
            i = 0
            bullet.update()
            if bullet.x > canvas_width - 80 or bullet.x < 80 or bullet.y > canvas_height - 80 or bullet.y < 80:
                bullet_list.pop(i)
            i += 1
    if particle_list.count is not 0:
        for par in particle_list:
            i = 0
            par.update()
            if par.cursize <= 0:
                particle_list.pop(i)
            i += 1
    delay(0.01)


def draw():
    clear_canvas()
    back_image.draw(canvas_width/2, canvas_height/2)
    # player.draw()
    if bullet_list.count is not 0:
        for bullet in bullet_list:
            bullet.draw()
    if particle_list.count is not 0:
        for par in particle_list:
            par.draw()
    player.draw()
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type is SDL_QUIT:
            game_framework.quit()
        elif event.type is SDL_KEYDOWN and event.key is SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_w):
            bullet_list.append(CBullet.Bullet(player))
        else:
            player.handle_event(event)


def pause():
    pass


def resume():
    pass
