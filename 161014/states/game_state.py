import random

from classes import CPlayer
from classes import CBullet
from classes import CEnemy
from classes import CParticle
from pico2d import *

from states import ranking_state
import game_framework

name = "GameState"
player0 = None
back_image = None
enemy_list = None
bullet_list = None
particle_list = None
canvas_boundary = 80
score = 0
time = 0

def enter():
    global player0, back_image, time, enemy_list, bullet_list, particle_list
    time = 0
    back_image = load_image('resource/image/back_gamestate.png')

    enemy_list = []
    bullet_list = []
    particle_list = []
    player0 = CPlayer.Player(1)


def exit():
    global player0, bullet_list, particle_list, enemy_list

    f = open('data_file.txt', 'r')
    score_data = json.load(f)
    f.close()

    score_data.append({"Score": score})

    print(score_data)

    f = open('data_file.txt', 'w')
    json.dump(score_data, f)
    f.close()


    del(player0)
    del(bullet_list)
    del(particle_list)
    del(enemy_list)


def update(frame_time):
    global player0, time, enemy_list, score, enemy_list, bullet_list, particle_list

    player0.update()


    if time % 3 is 0:
        particle_list.append(CParticle.Particle(player0.nozzle_x, player0.nozzle_y, 5))
    if time % player0.fire_rate is 0:
        bullet_list.append(CBullet.Bullet(player0))
    if time % 100 is 0:
        enemy_list.append(CEnemy.Enemy(random.randint(0, 3)))

    if bullet_list.count is not 0:
        for bullet in bullet_list:
            bullet.update()
            if bullet.isOut(get_canvas_width(), get_canvas_height(), canvas_boundary) or bullet.isCollide(player0):
                bullet_list.remove(bullet)
                continue
            if enemy_list.count is not 0:
                for enemy in enemy_list:
                    if bullet.isCollide(enemy):
                        bullet_list.remove(bullet)

    if enemy_list.count is not 0:
        for enemy in enemy_list:
            enemy.update()
            if enemy.isOut(get_canvas_width(), get_canvas_height(), canvas_boundary) or enemy.isCollide(player0):
                enemy_list.remove(enemy)
            if enemy.isDead():
                score += 10
                enemy_list.remove(enemy)
            if (enemy.kind is enemy.SHIP or enemy.kind is enemy.F_SHIP) and time % 3 is 0:
                particle_list.append(CParticle.Particle(enemy.nozzle_x, enemy.nozzle_y, 5))
            if enemy.kind is enemy.F_SHIP:
                enemy.Set_Theta(player0)

    if particle_list.count is not 0:
        for par in particle_list:
            par.update()
            if par.isEnd() or par.isOut(get_canvas_width(), get_canvas_height(), canvas_boundary):
                particle_list.remove(par)

    time += 1
    delay(0.01)
    if player0.isOut(get_canvas_width(), get_canvas_height(), canvas_boundary) or player0.isDead():
        game_framework.change_state(ranking_state)


def draw():
    global enemy_list, bullet_list, particle_list
    clear_canvas()
    # back_image.draw(canvas_width/2, canvas_height/2)
    back_image.clip_draw(canvas_boundary, 0, get_canvas_width() - 2 * canvas_boundary, get_canvas_height(), get_canvas_width()/2, get_canvas_height()/2)
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
    back_image.clip_draw(0, 0, canvas_boundary, get_canvas_height(), canvas_boundary/2, get_canvas_height()/2)
    back_image.clip_draw(get_canvas_width() - canvas_boundary, 0, canvas_boundary, get_canvas_height(), get_canvas_width() - canvas_boundary / 2, get_canvas_height()/2)
    player0.draw()
    update_canvas()


def handle_events(frame_time):
    global player0
    events = get_events()
    for event in events:
        if event.type is SDL_QUIT:
            game_framework.quit()
        elif event.type is SDL_KEYDOWN and event.key is SDLK_ESCAPE:
            game_framework.quit()
        else:
            player0.handle_event(event)


def pause():
    pass


def resume():
    pass
