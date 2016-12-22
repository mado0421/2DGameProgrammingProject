from pico2d import *
from Object import CObject
import random


class Particle(CObject.Object):

    def __init__(self, x, y, size):
        self.x, self.y, self.maxsize, self.cursize = x, y, size, size
        self.theta = math.radians(random.randint(0, 89))
        self.image = load_image('resource/image/particle.png')

    def update(self, frame_time):
        self.cursize -= 10 * frame_time

    def check_dead(self):
        if self.cursize < 0:
            return True
        return False

    def draw(self):
        self.image.opacify((self.cursize / self.maxsize))
        self.image.rotate_draw(self.theta, self.x, self.y, self.cursize, self.cursize)

