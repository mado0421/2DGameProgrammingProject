from pico2d import *
import game_framework
from Scene import rank_scene
from Object import CPlane
from Object import CPlayer
from Object import CAsteroid
from Object import CBullet
from Object import CParticle
import random

particle_list = []
player_list = []
bullet_list = []
asteroid_list = []
plane_list = []
score = 0
time = None
font = None
asteroid_timer = None
plane_timer = None
back_img = None


def enter():
    global font, back_img
    global time, asteroid_timer, plane_timer, score
    global asteroid_list, plane_list, player_list, bullet_list, particle_list
    particle_list = []
    player_list = []
    bullet_list = []
    asteroid_list = []
    plane_list = []
    time = 0
    score = 0
    asteroid_timer = 0
    plane_timer = 0
    font = load_font('Resource/font/RPGSystem.ttf', 50)
    back_img = load_image('resource/image/backimg.png')

    f = open('game_data.txt', 'r')
    game_data = json.load(f)
    f.close()

    if game_data[0] is 1:
        player_list.append(CPlayer.Player(0, game_data[1]))
    elif game_data[0] is 2:
        player_list.append(CPlayer.Player(1, game_data[1]))
        player_list.append(CPlayer.Player(2, game_data[2]))


def exit():

    f = open('data_score_file.txt', 'r')
    score_data = json.load(f)
    f.close()

    score_data.append({"Score": score})

    print(score_data)

    f = open('data_score_file.txt', 'w')
    json.dump(score_data, f)
    f.close()

    f = open('data_time_file.txt', 'r')
    score_data = json.load(f)
    f.close()

    score_data.append({"Score": time})

    print(score_data)

    f = open('data_time_file.txt', 'w')
    json.dump(score_data, f)
    f.close()

    pass


def update(frame_time):
    global time, asteroid_timer, plane_timer, score
    global asteroid_list, plane_list, particle_list

    time += frame_time
    asteroid_timer += frame_time
    plane_timer += frame_time

    if asteroid_timer > 2.0:
        asteroid_timer = 0
        asteroid_list.append(CAsteroid.Asteroid())

    if plane_timer > 2.5:
        plane_timer = 0
        if random.randint(0, 1) is 0:
            plane_list.append(CPlane.Plane())
        else:
            plane_list.append(CPlane.Follow_Plane())

    if len(player_list) is not 0:
        for player in player_list:
            if player.check_dead() is False:
                player.update(frame_time)
                player.particle_timer += frame_time
                if player.particle_timer > 0.1:
                    particle_list.append(CParticle.Particle(player.nozzle[0], player.nozzle[1], 10))
                    player.particle_timer = 0
                if player.check_out():
                    player_list.remove(player)
                if len(asteroid_list) is not 0:
                    for asteroid in asteroid_list:
                        if player.check_coll(asteroid):
                            player.hit(asteroid)
                            asteroid.hit(player)
                if len(plane_list) is not 0:
                    for plane in plane_list:
                        if player.check_coll(plane):
                            player.hit(plane)
                            plane.hit(player)
                if player.fire_timer > player.fire_rate:
                    player.fire_timer = 0
                    if player.bullet is 0 or player.bullet is 1:
                        bullet_list.append(CBullet.Bullet(player))
                    elif player.bullet is 2:
                        bullet_list.append(CBullet.Bullet(player))
                        player.theta -= math.radians(6)
                        bullet_list.append(CBullet.Bullet(player))
                        player.theta += math.radians(12)
                        bullet_list.append(CBullet.Bullet(player))
                        player.theta -= math.radians(6)
            else:
                player_list.remove(player)
    else:
        game_framework.change_state(rank_scene)

    if len(bullet_list) is not 0:
        for bullet in bullet_list:
            bullet.update(frame_time)
            if bullet.check_out():
                bullet_list.remove(bullet)
            elif bullet.check_dead():
                bullet_list.remove(bullet)
            else:
                if len(player_list) is not 0:
                    for player in player_list:
                        if bullet.check_coll(player):
                            bullet.hit(player)
                            player.hit(bullet)
                if len(asteroid_list) is not 0:
                    for asteroid in asteroid_list:
                        if bullet.check_coll(asteroid):
                            bullet.hit(asteroid)
                            asteroid.hit(bullet)
                if len(plane_list) is not 0:
                    for plane in plane_list:
                        if bullet.check_coll(plane):
                            bullet.hit(plane)
                            plane.hit(bullet)

    if len(asteroid_list) is not 0:
        for asteroid in asteroid_list:
            if asteroid.check_dead():
                score += 10
                asteroid_list.remove(asteroid)
            else:
                asteroid.update(frame_time)
                if asteroid.check_out():
                    asteroid_list.remove(asteroid)

    if len(plane_list) is not 0:
        for plane in plane_list:
            if plane.check_dead():
                score += 10
                plane_list.remove(plane)
            else:
                plane.particle_timer += frame_time
                if plane.particle_timer > 0.1:
                    particle_list.append(CParticle.Particle(plane.nozzle[0], plane.nozzle[1], 10))
                    plane.particle_timer = 0
                if type(plane) is CPlane.Follow_Plane:
                    if plane.state is CPlane.Follow_Plane.follow:
                        if plane.timer > plane.change_to_follow_time:
                            plane.state = plane.shoot
                            plane.timer = 0
                    else:
                        if plane.timer > plane.change_to_shoot_time:
                            bullet_list.append(CBullet.Bullet(plane))
                            plane.state = plane.follow
                            plane.timer = 0
                    if len(player_list) is not 0:
                        plane.set_theta(player_list[0])
                plane.update(frame_time)
                if plane.check_out() or plane.check_dead():
                    plane_list.remove(plane)

    if len(particle_list) is not 0:
        for particle in particle_list:
            particle.update(frame_time)
            if particle.check_dead():
                particle_list.remove(particle)


def draw():
    clear_canvas()
    back_img.draw(get_canvas_width()/2, get_canvas_height()/2)
    # font.draw(get_canvas_width()/2 - 90, get_canvas_height()/2 + 290, 'Plane: %5.1d' % len(plane_list), (230, 230, 255))

    font.draw(get_canvas_width()/2 - 250, get_canvas_height()/2 + 340, 'SCORE: %5.1d' % score, (230, 230, 255))
    font.draw(get_canvas_width()/2 + 50, get_canvas_height()/2 + 340, 'TIME: %5.1f' % time, (230, 230, 255))

    if len(player_list) is not 0:
        for player in player_list:
            player.draw()

    if len(bullet_list) is not 0:
        for bullet in bullet_list:
            bullet.draw()

    if len(asteroid_list) is not 0:
        for asteroid in asteroid_list:
            asteroid.draw()

    if len(plane_list) is not 0:
        for plane in plane_list:
            plane.draw()

    if len(particle_list) is not 0:
        for particle in particle_list:
            particle.draw()

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
