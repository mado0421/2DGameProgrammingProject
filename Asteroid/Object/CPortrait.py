from pico2d import load_image


class Portrait:

    char0, char1 = 0, 1

    def __init__(self, x, y, num_player):
        self.x, self.y = x, y
        self.char_frame = load_image('Resource/image/char_frame.png')
        self.ship_frame = load_image('Resource/image/ship_frame.png')
        self.char_img = load_image('Resource/image/char_%d.png' % num_player)
        self.ship_img = load_image('Resource/image/ship%d.png' % num_player)
        if num_player is self.char0:
            self.speed = 4
            self.rotate = 2
        elif num_player is self.char1:
            self.speed = 3
            self.rotate = 3

    def draw(self):
        self.char_frame.draw(self.x, self.y)
        self.char_img.draw(self.x, self.y)
        self.ship_frame.draw(self.x, self.y)
        self.ship_img.draw(self.x - 58, self.y - 65)

