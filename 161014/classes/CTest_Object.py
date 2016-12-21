class Object:

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.size = 0

    def checkColl(self, other):
        if self.x - self.size < other.x + other.size and\
            self.x + self.size > other.x - other.size and\
            self.y - self.size < other.y + other.size and\
                self.y + self.size > other.y - other.size:
                return True
        return False


class Asteroid(Object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0


class Plane(Object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0


class Bullet(Object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0

