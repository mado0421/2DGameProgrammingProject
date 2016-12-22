from Object import CObject
from pico2d import *


class Bullet(CObject.Object):

    default, long, round = 0, 1, 2

    def __init__(self, gunner):
        self.x = gunner.barrel.y
        self.y = gunner.barrel.x
        if gunner.bullet is self.default:
            self.size = 5
            self.speed = 500
            self.damage = 1
        elif gunner.bullet is self.long:
            self.size = 5
            self.speed = 800
            self.damage = 2
        elif gunner.bullet is self.round:
            self.size = 10
            self.speed = 400
            self.damage = 1
        self.team = gunner.team
        self.theta = gunner.theta

    def update(self, frame_time):
        self.x += math.cos(self.theta) * self.speed * frame_time
        self.y += math.sin(self.theta) * self.speed * frame_time
