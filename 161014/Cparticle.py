from pico2d import *
import random


class Particle:
    def __init__(self, x, y, size):
        self.x, self.y, self.maxsize, self.cursize = x, y, size, size
        self.theta = math.radians(random.randint(0, 89))
        self.image = load_image('resource/image/particle.png')

    def update(self):
        self.cursize -= 0.1
        self.image.opacify(self.cursize / self.maxsize)

    def draw(self):
        self.image.rotate_draw(self.theta, self.x, self.y, self.cursize, self.cursize)
