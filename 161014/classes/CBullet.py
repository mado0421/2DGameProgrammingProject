from pico2d import *


class Bullet:

    ROUND, LONG = 0, 1

    def __init__(self, parent):
        self.theta, self.team, self.kind = parent.theta, parent.team, parent.bullet_type
        self.x, self.y = parent.barrel_x, parent.barrel_y

        if self.kind is self.ROUND:
            self.speed = 5.2
            self.width = 2
            self.damage = 1

        elif self.kind is self.LONG:
            self.speed = 6.7
            self.width = 2
            self.damage = 2

        self.image = load_image('resource/image/bullet%d.png' % self.kind)
        # if Bullet.image is None:
            # Bullet.image = load_image('resource/image/bullet%d.png' % self.kind)

    def isDead(self):
        if self.health <= 0:
            return True

    def isOut(self, cw, ch, cb):
        if self.x > cw - cb or self.x < cb or self.y > ch - cb or self.y < cb:
            return True

    def isCollide(self, other):
        if self.team is not other.team:
            if (self.x - self.width <= other.x + other.width and
                self.y - self.width <= other.y + other.width and
                self.x + self.width >= other.x - other.width and
                self.y + self.width >= other.y - other.width):
                    other.health -= self.damage
                    return True

    def update(self):
        self.x += math.cos(self.theta) * self.speed
        self.y += math.sin(self.theta) * self.speed

    def draw(self):
        self.image.rotate_draw(self.theta - math.radians(90), self.x, self.y, None, None)
        #draw_rectangle(self.x - self.width, self.y - self.width, self.x + self.width, self.y + self.width)