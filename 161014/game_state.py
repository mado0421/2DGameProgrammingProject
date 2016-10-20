from pico2d import *
import random
import CPlayer
import CBullet
import CParticle
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
canvas_boundary = 80


def enter():
    global player0
    global back_image
    global time
    time = 0
    open_canvas(canvas_width, canvas_height, sync=True)
    back_image = load_image('resource/image/back_gamestate.png')
    player0 = CPlayer.Player(1)


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
    if player0.isOut(canvas_width, canvas_height, canvas_boundary) or player0.isDead():
        game_framework.quit()

    if time % 3 is 0:
        particle_list.append(CParticle.Particle(player0.nozzle_x, player0.nozzle_y, 5))
    if time % player0.fire_rate is 0:
        bullet_list.append(CBullet.Bullet(player0))
    if time % 100 is 0:
        # enemy_list.append(CEnemy.Enemy(random.randint(0, 2)))
        enemy_list.append(CEnemy.Enemy(random.randint(0, 3)))

    if bullet_list.count is not 0:
        for bullet in bullet_list:
            bullet.update()
            if enemy_list.count is not 0:
                for enemy in enemy_list:
                    if bullet.isCollide(enemy):
                        bullet_list.remove(bullet)
                        continue
            if bullet.isOut(canvas_width, canvas_height, canvas_boundary) or bullet.isCollide(player0):
                bullet_list.remove(bullet)

    if enemy_list.count is not 0:
        for enemy in enemy_list:
            enemy.update()
            if enemy.isOut(canvas_width, canvas_height, canvas_boundary) or enemy.isDead() or enemy.isCollide(player0):
                enemy_list.remove(enemy)
            if (enemy.kind is enemy.SHIP or enemy.kind is enemy.F_SHIP) and time % 3 is 0:
                particle_list.append(CParticle.Particle(enemy.nozzle_x, enemy.nozzle_y, 5))

    if particle_list.count is not 0:
        for par in particle_list:
            par.update()
            if par.isEnd() or par.isOut(canvas_width, canvas_height, canvas_boundary):
                particle_list.remove(par)

    time += 1
    delay(0.01)


def draw():
    clear_canvas()
    # back_image.draw(canvas_width/2, canvas_height/2)
    back_image.clip_draw(canvas_boundary, 0, canvas_width - 2 * canvas_boundary, canvas_height, canvas_width/2, canvas_height/2)
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
    back_image.clip_draw(0, 0, canvas_boundary, canvas_height, canvas_boundary / 2, canvas_height/2)
    back_image.clip_draw(canvas_width - canvas_boundary, 0, canvas_boundary, canvas_height, canvas_width - canvas_boundary / 2, canvas_height/2)
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
