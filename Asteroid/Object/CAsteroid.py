from Object import CObject
from pico2d import *
import random


class Asteroid(CObject.Object):

    left, right = 0, 1

    def __init__(self):
        self.way = random.randint(self.left, self.right)
        if self.way is self.left:
            self.x = 50
            self.y = random.randint(50, get_canvas_height() - 50)
        elif self.way is self.right:
            self.x = get_canvas_width() - 50
            self.y = random.randint(50, get_canvas_height() - 50)
        self.img = load_image('Resource/image/enemy0.png')
        self.size = 20
        self.speed = 50
        self.team = 0
        self.health = 3
        self.damage = 10

    def update(self, frame_time):
        if self.way is self.left:
            self.x += self.speed * frame_time
        else:
            self.x -= self.speed * frame_time

    def draw(self):
        self.img.draw(self.x, self.y)
        # draw_rectangle(self.x - self.size, self.y - self.size, self.x + self.size, self.y + self.size)

