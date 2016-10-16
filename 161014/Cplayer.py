from pico2d import *
import CBullet
import os


class Player:
    image = None

    FORWARD, LEFT, RIGHT = 0, 1, 2
    CHAR1, CHAR2, CHAR3 = 0, 1, 2
    ROUND, LONG = 0, 1

    def __init__(self, kind):
        self.kind = kind
        self.team = 0
        self.theta = math.radians(90)
        self.state = self.FORWARD
        self.x, self.y = 400, 300
        if kind is self.CHAR1:
            self.width = 16
            self.height = 40
            self.speed = 2.4
            self.dtheta = 2.4
            self.bullet_type = self.ROUND
        self.barrel_x = self.x + math.cos(self.theta) * self.width
        self.barrel_y = self. y + math.sin(self.theta) * self.height
        if Player.image is None:
            os.chdir('resource/image')
            Player.image = load_image('ship%d.png' % self.kind)
            os.chdir('../..')

    def update(self):
        if self.state is self.RIGHT:
            self.theta -= math.radians(self.dtheta)
        elif self.state is self.LEFT:
            self.theta += math.radians(self.dtheta)
        self.x += math.cos(self.theta) * self.speed
        self.y += math.sin(self.theta) * self.speed

    def draw(self):
        self.image.rotate_draw(self.theta - math.radians(90), self.x, self.y, None, None)

    def handle_event(self, event):
        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            self.state = self.LEFT
        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_d):
            self.state = self.RIGHT
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_a):
            if self.state is self.LEFT:
                self.state = self.FORWARD
        elif(event.type, event.key) == (SDL_KEYUP, SDLK_d):
            if self.state is self.RIGHT:
                self.state = self.FORWARD
        # elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_w):
