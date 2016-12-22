from pico2d import load_image


class Portrait:
    def __init__(self, x, y, num_player):
        self.x, self.y = x, y
        self.char_frame = load_image('Resource/image/char_frame.png')
        self.ship_frame = load_image('Resource/image/ship_frame.png')
        self.char_img = load_image('Resource/image/char_%d.png' % num_player)
        self.ship_img = load_image('Resource/image/ship%d.png' % num_player)

    def draw(self):
        self.char_frame.draw(self.x, self.y)
        self.char_img.draw(self.x, self.y)
        self.ship_frame.draw(self.x, self.y)
        self.ship_img.draw(self.x - 58, self.y - 65)

