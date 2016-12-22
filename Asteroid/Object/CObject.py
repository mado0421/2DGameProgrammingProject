from pico2d import draw_rectangle
from pico2d import get_canvas_width
from pico2d import get_canvas_height


class Object:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 0
        self.team = 0
        self.health = 1
        self.live = True

    def draw(self):
        draw_rectangle(self.x - self.size, self.y - self.size, self.x + self.size, self.y + self.size)

    def update(self, frame_time):
        pass

    def check_coll(self, other):
        if self.team != other.team:
            if self.x - self.size < other.x + other.size and\
                    self.x + self.size > other.x - other.size:
                if self.y - self.size < other.y + other.size and\
                        self.y + self.size > other.y - other.size:
                    return True
        return False

    def check_out(self):
        if get_canvas_width() - 50 < self.x - self.size or\
                self.x + self.size < 50:
            return True
        if get_canvas_height() - 50 < self.y - self.size or\
                self.y + self.size < 50:
            return True
        return False

    def check_dead(self):
        if self.health <= 0:
            return True
        return False

    def hit(self, other):
        self.health -= other.damage
