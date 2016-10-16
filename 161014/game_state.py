from Cplayer import *
import CBullet
import game_framework

name = "GameState"
player = None
# bullet = None


def enter():
    global player
    # global bullet
    open_canvas()
    player = Player(0)
    # bullet = CBullet.Bullet(2, 0, 45, 400, 300)


def exit():
    global player
    # global bullet
    del(player)
    # del(bullet)
    close_canvas()


def update():
    player.update()
    # bullet.update()
    delay(0.01)


def draw():
    clear_canvas()
    player.draw()
    # bullet.draw()
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type is SDL_QUIT:
            game_framework.quit()
        elif event.type is SDL_KEYDOWN and event.key is SDLK_ESCAPE:
            game_framework.quit()
        else:
            player.handle_event(event)


def pause():
    pass


def resume():
    pass
