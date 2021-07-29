import time

from gyminput import check_input
from gymdisplay import set_display, set_display_individual
from gymbuzz import beep

def up_timer(max_second, refresh_rate):
    start = time.time()
    while True:
        if check_input():
            return False
        current = int(time.time() - start)
        set_display(current)
        if current >= max_second:
            return True
        time.sleep(refresh_rate)

def up_timer_interval(start, interval, max_second, refresh_rate):
    while True:
        if check_input():
            return False
        current = int(time.time() - start)
        tens = int(current / 10)
        ones = int(current % 10)
        set_display_individual(str(interval), 'h', True, str(tens), str(ones))
        if current >= max_second:
            return True
        time.sleep(refresh_rate)

def down_timer(max_second, refresh_rate):
    end = time.time() + max_second
    while True:
        if check_input():
            return False
        current = int(end - time.time())
        set_display(current)
        if current <= 0:
            return True
        time.sleep(refresh_rate)

# EMOM style
def every_x_for_y(x, y, beep_time, refresh_rate):
    for a in range(y):
        start = time.time()
        if not up_timer_interval(start, a + 1, x, refresh_rate):
            return False
        beep(beep_time)

    return True

# Tabata style
def every_x_and_y_for_z(x, y, z, beep_time, refresh_rate):
    for a in range(z):
        start = time.time()
        if not up_timer_interval(start, a + 1, x, refresh_rate):
            return False
        beep(beep_time)
        start = time.time()
        if not up_timer_interval(start, a + 1, y, refresh_rate):
            return False
        beep(2 * beep_time)

    return True
