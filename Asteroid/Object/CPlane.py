from Object import CObject
from pico2d import *
import random


class Plane(CObject.Object):

    left, right = 0, 1

    def __init__(self):
        self.way = random.randint(self.left, self.right)

        if self.way is self.left:
            self.x = 50
            self.y = random.randint(50, get_canvas_height() - 50)
            self.theta = math.radians(0)
        elif self.way is self.right:
            self.x = get_canvas_width() - 50
            self.y = random.randint(50, get_canvas_height() - 50)
            self.theta = math.radians(180)
        self.img = load_image('Resource/image/enemy2.png')
        self.size = 20
        self.speed = 80
        self.team = 0
        self.health = 2
        self.damage = 10
        self.barrel = [self.x + math.cos(self.theta) * self.size, self.y + math.sin(self.theta) * self.size]
        self.nozzle = [self.x - math.cos(self.theta) * self.size, self.y - math.sin(self.theta) * self.size]

    def update(self, frame_time):
        self.x += math.cos(self.theta) * self.speed * frame_time
        self.y += math.sin(self.theta) * self.speed * frame_time
        self.barrel = [self.x + math.cos(self.theta) * self.size, self.y + math.sin(self.theta) * self.size]
        self.nozzle = [self.x - math.cos(self.theta) * self.size, self.y - math.sin(self.theta) * self.size]

    def draw(self):
        self.img.rotate_draw(self.theta - math.radians(90), self.x, self.y, None, None)
        draw_rectangle(self.x - self.size, self.y - self.size, self.x + self.size, self.y + self.size)


class Follow_Plane(Plane):

    follow, shoot = 0, 1
    enemy_bullet = 3

    def __init__(self):
        Plane.__init__(self)
        self.state = self.follow
        self.change_to_follow_time = 3
        self.change_to_shoot_time = 1
        self.timer = 0
        self.speed = 60
        self.bullet = self.enemy_bullet
        self.img = load_image('Resource/image/enemy3.png')

    def update(self, frame_time):
        self.timer += frame_time
        if self.state is self.follow:
            Plane.update(self, frame_time)
        elif self.state is self.shoot:
            pass

    def set_theta(self, other):
        w = self.x - other.x
        h = self.y - other.y
        r = math.sqrt(w * w + h * h)
        if r is 0:
            self.theta = 0
        else:
            if w < 0:
                if h < 0:
                    self.theta = -math.acos(w/r) + math.radians(180)
                elif h > 0:
                    self.theta = math.acos(w/r) + math.radians(180)
                else:
                    self.theta = 0
            elif w > 0:
                if h < 0:
                    self.theta = -math.acos(w/r) + math.radians(180)
                elif h > 0:
                    self.theta = math.acos(w/r) + math.radians(180)
                else:
                    self.theta = math.radians(180)
            elif w is 0:
                if h < 0:
                    self.theta = math.radians(90)
                elif h > 0:
                    self.theta = math.radians(270)

