class Timer:
    def __init__(self):
        self.time = 0

    def update(self, frame_time):
        self.time += frame_time
        if (self.time / 16) is 1:
            self.time -= 16
            return True
        else:
            return False
