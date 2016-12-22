from Object import CObject
from pico2d import *


class Bullet(CObject.Object):

    default, long, round, enemy_bullet = 0, 1, 2, 3

    def __init__(self, gunner):
        self.x = gunner.barrel[0]
        self.y = gunner.barrel[1]
        if gunner.bullet is self.default:
            self.size = 10
            self.speed = 500
            self.damage = 1
            self.img = load_image('Resource/image/bullet0.png')
        elif gunner.bullet is self.long:
            self.size = 10
            self.speed = 800
            self.damage = 3
            self.img = load_image('Resource/image/bullet1.png')
        elif gunner.bullet is self.round:
            self.size = 8
            self.speed = 300
            self.damage = 1
            self.img = load_image('Resource/image/bullet2.png')
        elif gunner.bullet is self.enemy_bullet:
            self.size = 10
            self.speed = 200
            self.damage = 1.5
            self.img = load_image('Resource/image/bullet3.png')
        self.team = gunner.team
        self.theta = gunner.theta
        self.health = 1

    def update(self, frame_time):
        self.x += math.cos(self.theta) * self.speed * frame_time
        self.y += math.sin(self.theta) * self.speed * frame_time

    def draw(self):
        self.img.rotate_draw(self.theta - math.radians(90), self.x, self.y, None, None)
        draw_rectangle(self.x - self.size, self.y - self.size, self.x + self.size, self.y + self.size)
