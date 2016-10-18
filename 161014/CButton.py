from pico2d import *


class Button:
    def __init__(self, name, x, y):
        self.on_image = load_image('resource/image/button/on_%s.png' % name)
        self.off_image = load_image('resource/image/button/off_%s.png' % name)
        self.width = 172
        self.height = 30
        self.x, self.y = x, y
        self.on = False

    def update(self):
        pass

    def handle_event(self, event):
        if event.type is SDL_MOUSEMOTION:
            pass

    def draw(self):
        if self.on is True:
            self.on_image.draw_now(self.x, self.y, self.width, self.height)
        else:
            self.off_image.draw_now(self.x, self.y, self.width, self.height)