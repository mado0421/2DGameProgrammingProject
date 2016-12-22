from Object import CObject
from pico2d import get_canvas_width
from pico2d import get_canvas_height
import random


class Plane(CObject.Object):

    left, right = 0, 1

    def __init__(self):
        self.way = random.randint(self.left, self.right)
        self.x = get_canvas_width() * self.way
        self.y = random.randint(0, get_canvas_height())
        self.size = 10
        self.speed = 200
        self.team = 0
        self.health = 2
        self.damage = 10

    def update(self, frame_time):
        if self.way is self.left:
            self.x += self.speed * frame_time
        else:
            self.x -= self.speed * frame_time
