from pico2d import *


class Player:
    # PIXEL_PER_METER = (10.0 / 0.3)
    # RUN_SPEED_KMPH = 20.0
    # RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    # RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    # RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    FORWARD, LEFT, RIGHT = 0, 1, 2
    CHAR1, CHAR2, CHAR3 = 0, 1, 2
    ROUND, LONG = 0, 1

    def __init__(self, kind):
        self.kind = kind
        self.image = load_image('resource/image/ship%d.png' % self.kind)
        self.team = 0
        self.theta = math.radians(90)
        self.state = self.FORWARD
        self.health = 1
        if kind is self.CHAR1:
            self.x, self.y = get_canvas_width()/2, get_canvas_height()/2
            self.width = 18
            self.height = 25
            self.speed = 3.5
            self.dtheta = 4.5
            self.bullet_type = self.ROUND
            self.fire_rate = 15
        if kind is self.CHAR2:
            self.x, self.y = get_canvas_width()/2, get_canvas_height()/2
            self.width = 18
            self.height = 29
            self.speed = 3.2
            self.dtheta = 4.0
            self.bullet_type = self.LONG
            self.fire_rate = 45
        self.barrel_x = self.x + math.cos(self.theta) * self.height
        self.barrel_y = self.y + math.sin(self.theta) * self.height
        self.nozzle_x = self.x - math.cos(self.theta) * self.height
        self.nozzle_y = self.y - math.sin(self.theta) * self.height
        # if Player.image is None:
            # Player.image = load_image('resource/image/ship%d.png' % self.kind)

    def update(self):
        if self.state is self.RIGHT:
            self.theta -= math.radians(self.dtheta)
        elif self.state is self.LEFT:
            self.theta += math.radians(self.dtheta)

        # distance = Player.RUN_SPEED_PPS * frame_time
        # self.total_frames += 1.0

        self.x += math.cos(self.theta) * self.speed  # * distance
        self.y += math.sin(self.theta) * self.speed  # * distance
        self.barrel_x = self.x + math.cos(self.theta) * self.height
        self.barrel_y = self.y + math.sin(self.theta) * self.height
        self.nozzle_x = self.x - math.cos(self.theta) * self.height
        self.nozzle_y = self.y - math.sin(self.theta) * self.height

    def isDead(self):
        if self.health <= 0:
            return True

    def isOut(self, cw, ch, cb):
        if self.x + self.width > cw - cb or self.x - self.width < cb or\
            self.y + self.height > ch - cb or self.y - self.height < cb:
            return True

    def draw(self):
        self.image.rotate_draw(self.theta - math.radians(90), self.x, self.y, None, None)
        #draw_rectangle(self.x - self.width, self.y - self.width, self.x + self.width, self.y + self.width)

    def handle_event(self, event):
        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            self.state = self.LEFT
        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_d):
            self.state = self.RIGHT
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_a):
            if self.state is self.LEFT:
                self.state = self.FORWARD
        elif(event.type, event.key) == (SDL_KEYUP, SDLK_d):
            if self.state is self.RIGHT:
                self.state = self.FORWARD
