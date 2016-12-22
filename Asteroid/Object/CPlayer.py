from Object import CObject
from pico2d import get_canvas_width
from pico2d import get_canvas_height
from pico2d import math


class Player(CObject.Object):

    forward, left, right = 0, 1, 2
    default, long, round = 0, 1, 2

    def __init__(self, num_player, ship_kind):
        if num_player is 0:
            self.x = get_canvas_width() / 2
        elif num_player is 1:
            self.x = get_canvas_width() / 4 * 1
        elif num_player is 2:
            self.x = get_canvas_width() / 2 * 3
        self.y = get_canvas_height() / 3

        self.theta = math.radians(90)

        if ship_kind is 1:
            self.dtheta = 4.5
        elif ship_kind is 2:
            self.dtheta = 4.0

        self.way = self.forward
        self.bullet = self.default
        self.size = 10
        self.speed = 200
        self.team = 0

    def update(self, frame_time):

        if self.way is self.right:
            self.theta -= math.radians(self.dtheta)
        elif self.way is self.left:
            self.theta += math.radians(self.dtheta)

        self.x += math.cos(self.theta) * self.speed  # * distance
        self.y += math.sin(self.theta) * self.speed  # * distance


