from pico2d import *
from Object import CObject
import random


class Player(CObject.Object):

    solo, p1, p2 = 0, 1, 2
    ship1, ship2 = 0, 1
    forward, left, right = 0, 1, 2
    default, long, round = 0, 1, 2

    def __init__(self, num_player, ship_kind):
        self.num_player = num_player
        if num_player is self.solo:
            self.x = get_canvas_width() / 2
        elif num_player is self.p1:
            self.x = get_canvas_width() / 4 * 1
        elif num_player is self.p2:
            self.x = get_canvas_width() / 4 * 3
        self.y = get_canvas_height() / 3

        self.theta = math.radians(90)
        if ship_kind is self.ship1:
            self.speed = 200
            self.dtheta = 0.5
            self.img = load_image('Resource/image/ship0.png')
        elif ship_kind is self.ship2:
            self.speed = 170
            self.dtheta = 0.8
            self.img = load_image('Resource/image/ship1.png')

        self.way = self.forward
        self.bullet = random.randint(0, 2)
        if self.bullet is self.default:
            self.fire_rate = 0.3
        elif self.bullet is self.long:
            self.fire_rate = 0.5
        elif self.bullet is self.round:
            self.fire_rate = 0.8
        self.fire_timer = 0
        self.size = 10
        self.team = 1
        self.particle_timer = 0
        self.damage = 10
        self.health = 1
        self.barrel = [self.x + math.cos(self.theta) * self.size, self.y + math.sin(self.theta) * self.size]
        self.nozzle = [self.x - math.cos(self.theta) * self.size, self.y - math.sin(self.theta) * self.size]

    def update(self, frame_time):

        if self.way is self.right:
            self.theta -= math.radians(self.dtheta)
        elif self.way is self.left:
            self.theta += math.radians(self.dtheta)

        self.x += math.cos(self.theta) * self.speed * frame_time
        self.y += math.sin(self.theta) * self.speed * frame_time
        self.barrel = [self.x + math.cos(self.theta) * self.size, self.y + math.sin(self.theta) * self.size]
        self.nozzle = [self.x - math.cos(self.theta) * self.size, self.y - math.sin(self.theta) * self.size]
        self.fire_timer += frame_time

    def handle_events(self, event):
        if self.num_player is self.p1 or self.num_player is self.solo:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
                self.way = self.left
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_d):
                self.way = self.right
            elif (event.type, event.key) == (SDL_KEYUP, SDLK_a):
                if self.way is self.left:
                    self.way = self.forward
            elif (event.type, event.key) == (SDL_KEYUP, SDLK_d):
                if self.way is self.right:
                    self.way = self.forward
        elif self.num_player is self.p2:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_j):
                self.way = self.left
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_l):
                self.way = self.right
            elif (event.type, event.key) == (SDL_KEYUP, SDLK_j):
                if self.way is self.left:
                    self.way = self.forward
            elif (event.type, event.key) == (SDL_KEYUP, SDLK_l):
                if self.way is self.right:
                    self.way = self.forward

    def draw(self):
        self.img.rotate_draw(self.theta - math.radians(90), self.x, self.y, None, None)
        # draw_rectangle(self.x - self.size, self.y - self.size, self.x + self.size, self.y + self.size)
