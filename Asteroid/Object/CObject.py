from pico2d import draw_rectangle


class Object:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 0
        self.team = 0

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
