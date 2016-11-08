import pico2d

x = 0

while(True):
    current_time = pico2d.get_time()

    x += 5

    frame_time = pico2d.get_time() - current_time
    print("%f sec" % frame_time)

    current_time += frame_time
