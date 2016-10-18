from pico2d import *
import random


class Enemy:

    ROCK, BIG_ROCK, SHIP, F_SHIP = 0, 1, 2, 3

    def __init__(self, kind):
        self.kind = kind
        self.image = load_image('resource/image/enemy%d.png' % self.kind)
        self.team = 1
        self.theta = math.radians(random.randint(0, 90))

        if kind is Enemy.ROCK:
            self.width = 32
            self.height = 32
            self.speed = 1
        elif kind is Enemy.BIG_ROCK:
            self.width = 64
            self.height = 64
            self.speed = 1

        if random.randint(0, 1) is 0:
            self.way = 1
            self.x = (-self.width)
        else:
            self.way = -1
            self.x = 1280 + self.width

        self.y = random.randint(self.height, 800 - self.height)

    def update(self):
        self.x += self.way * self.speed

    def draw(self):
        self.image.rotate_draw(self.theta, self.x, self.y, None, None)
