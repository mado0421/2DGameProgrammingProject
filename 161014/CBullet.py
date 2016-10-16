from pico2d import *


class Bullet:
    image = None

    ROUND, LONG = 0, 1

    def __init__(self, parent):
        self.theta, self.team, self.kind = parent.theta, parent.team, parent.bullet_type
        self.x, self.y = parent.barrel_x, parent.barrel_y
        if self.kind is self.ROUND:
            self.speed = 3.5
        elif self.kind is self.LONG:
            self.speed = 4.8
        if Bullet.image is None:
            Bullet.image = load_image('resource/image/bullet%d.png' % self.kind)

    def update(self):
        self.x += math.cos(self.theta) * self.speed
        self.y += math.sin(self.theta) * self.speed

    def draw(self):
        self.image.rotate_draw(self.theta - math.radians(90), self.x, self.y, None, None)
