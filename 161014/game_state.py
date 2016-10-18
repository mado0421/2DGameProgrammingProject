from pico2d import *
import random
import Cplayer
import CBullet
import Cparticle
import CEnemy
import game_framework

name = "GameState"
player0 = None
back_image = None
time = None
enemy_list = []
bullet_list = []
particle_list = []
canvas_width = 1280
canvas_height = 800


def enter():
    global player0
    global back_image
    global time
    time = 0
    open_canvas(canvas_width, canvas_height, sync=True)
    back_image = load_image('resource/image/back_gamestate.png')
    player0 = Cplayer.Player(1)


def exit():
    global player0
    global bullet_list, particle_list, enemy_list
    del(player0)
    del(bullet_list)
    del(particle_list)
    del(enemy_list)
    close_canvas()


def update():
    global time, enemy_list
    player0.update()
    if time % 3 is 0:
        particle_list.append(Cparticle.Particle(player0.nozzle_x, player0.nozzle_y, 5))
    if time % player0.fire_rate is 0:
        bullet_list.append(CBullet.Bullet(player0))
    if time % 100 is 0:
        enemy_list.append(CEnemy.Enemy(random.randint(0, 1)))

    if bullet_list.count is not 0:
        for bullet in bullet_list:
            bullet.update()
            if bullet.x > canvas_width - 80 or bullet.x < 80 or bullet.y > canvas_height - 80 or bullet.y < 80:
                bullet_list.remove(bullet)
    if particle_list.count is not 0:
        for par in particle_list:
            par.update()
            if par.cursize <= 0:
                particle_list.remove(par)
    if enemy_list.count is not 0:
        for enemy in enemy_list:
            enemy.update()
            if not (0 - enemy.width <= enemy.x <= canvas_width + enemy.width):
                enemy_list.remove(enemy)

    time += 1
    delay(0.01)


def draw():
    clear_canvas()
    back_image.draw(canvas_width/2, canvas_height/2)
    # player.draw()
    if enemy_list.count is not 0:
        for enemy in enemy_list:
            enemy.draw()
    if bullet_list.count is not 0:
        for bullet in bullet_list:
            bullet.draw()
    if particle_list.count is not 0:
        for par in particle_list:
            par.draw()
    player0.draw()
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type is SDL_QUIT:
            game_framework.quit()
        elif event.type is SDL_KEYDOWN and event.key is SDLK_ESCAPE:
            game_framework.quit()
        # elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_w):
            # bullet_list.append(CBullet.Bullet(player))
        else:
            player0.handle_event(event)


def pause():
    pass


def resume():
    pass
