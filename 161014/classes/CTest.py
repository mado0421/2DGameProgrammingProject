import pico2d


class Test_frame:

    def __init__(self):
        self.x = 10
        self.y = 300
        self.speed = 50

    def update(self, frame_time):
        distance = frame_time * self.speed
        self.x += distance

    def draw(self):
        pico2d.draw_rectangle(self.x - 10, self.y - 10, self.x + 10, self.y + 10)
