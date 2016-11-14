import pico2d
from classes import CTest
from classes import CTest_timer
from classes import CParticle

name = "TestState"
Test_obj = None
Timer = None
particle_list = []


def enter():
    global Test_obj, Timer
    Test_obj = CTest.Test_frame()
    Timer = CTest_timer.Timer()


def exit():
    global Test_obj, Timer, particle_list
    del(particle_list)
    del(Timer)
    del(Test_obj)


def update(frame_time):
    global Test_obj, Timer
    Timer.update(frame_time)
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
