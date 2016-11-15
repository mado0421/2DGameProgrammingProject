from pico2d import *


class Button:

    def __init__(self, name, x, y, tag):
        self.name, self.x, self.y, self.tag = name, x, y, tag
        self.off_image = load_image('resource/image/Button/off_%s.png' % self.name)
        self.on_image = load_image('resource/image/Button/on_%s.png' % self.name)
        self.w, self.h = self.off_image.get_w_h()
        self.on_switch = False


    def update(self):
        pass

    def handle_event(self, event):
        if event.type == SDL_MOUSEMOTION:
            if self.is_on(event.x, get_canvas_height() - event.y):
                self.on_switch = True
            else:
                self.on_switch = False

    def draw(self):
        if self.on_switch is True:
            self.on_image.draw(self.x, self.y)
        else:
            self.off_image.draw(self.x, self.y)

    def is_on(self, x, y):
        if (self.x - self.w < x) and (x < self.x + self.w) and (self.y - self.h < y) and (y < self.y + self.h):
            return True
        return False

