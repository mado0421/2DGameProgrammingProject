from pico2d import *
import random


class Enemy:

    ROCK, BIG_ROCK, SHIP, F_SHIP = 0, 1, 2, 3

    def __init__(self, kind):
        self.kind = kind
        self.image = load_image('resource/image/enemy%d.png' % self.kind)
        self.team = 1
        self.theta = math.radians(0)

        if kind is Enemy.ROCK:
            self.width = 32
            self.height = 32
            self.speed = 1.2
        elif kind is Enemy.BIG_ROCK:
            self.width = 64
            self.height = 64
            self.speed = 0.6
        elif kind is Enemy.SHIP:
            self.width = 17
            self.height = 28
            self.speed = 1.4
        elif kind is Enemy.F_SHIP:
            self.width = 25
            self.height = 23
            self.speed = 1.8

        if random.randint(0, 1) is 0:
            self.way = 1
            self.x = (-self.width)
            self.theta = math.radians(0)
        else:
            self.way = -1
            self.x = 1280 + self.width
            self.theta = math.radians(180)

        self.y = random.randint(self.height + 80, 720 - self.height)
        self.barrel_x = self.x + math.cos(self.theta) * self.height
        self.barrel_y = self.y + math.sin(self.theta) * self.height
        self.nozzle_x = self.x - math.cos(self.theta) * self.height
        self.nozzle_y = self.y - math.sin(self.theta) * self.height

    def update(self):
        self.x += self.way * self.speed
        if self.kind is Enemy.ROCK or self.kind is Enemy.BIG_ROCK:
            self.theta += math.radians(2.2)
        else:
            self.nozzle_x = self.x - math.cos(self.theta) * self.height
            self.nozzle_y = self.y - math.sin(self.theta) * self.height

    def draw(self):
        self.image.rotate_draw(self.theta - math.radians(90), self.x, self.y)
        draw_rectangle(self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height)