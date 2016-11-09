import pico2d
from classes import CTest

name = "TestState"
Test_obj = None


def enter():
    global Test_obj
    Test_obj = CTest.Test_frame()


def exit():
    global Test_obj
    del(Test_obj)


def update(frame_time):
    global Test_obj
    Test_obj.update(frame_time)


def draw():
    global Test_obj
    pico2d.clear_canvas()

    Test_obj.draw()

    pico2d.update_canvas()


def handle_events(frame_time):
    events = pico2d.get_events()


def pause():
    pass


def resume():
    pass
