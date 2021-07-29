import time

from gymbuzz import beep
from gyminput import read_input, parse_input
from gymdisplay import marquee_once, clear_display
from gymtimer import up_timer, down_timer, every_x_for_y, every_x_and_y_for_z

refresh_rate = 0.1
beep_time = 0.3

marquee_once("1234567890    ")

def check_options():
    try:
        params = parse_input()
        print(params)
        if params[0] == "stop":
            clear_display()

        elif params[0] == "up":
            if not down_timer(10, refresh_rate):
                return check_options()
            beep(beep_time)
            if not up_timer(params[1], refresh_rate):
                return check_options()
            beep(beep_time)
            time.sleep(2)
            clear_display()

        elif params[0] == "down":
            if not down_timer(10, refresh_rate):
                return check_options()
            beep(beep_time)
            if not down_timer(params[1], refresh_rate):
                return check_options()
            beep(beep_time)
            time.sleep(2)
            clear_display()

        elif params[0] == "emom":
            if not down_timer(10, refresh_rate):
                return check_options()
            beep(beep_time)
            if not every_x_for_y(60, params[1], beep_time, refresh_rate):
                return check_options()
            beep(beep_time)
            time.sleep(2)
            clear_display()

        elif params[0] == "every" and len(params) < 4:
            if not down_timer(10, refresh_rate):
                return check_options()
            beep(beep_time)
            if not every_x_for_y(params[1], params[2], beep_time, refresh_rate):
                return check_options()
            beep(beep_time)
            time.sleep(2)
            clear_display()

        elif params[0] == "every":
            if not down_timer(10, refresh_rate):
                return check_options()
            beep(beep_time)
            if not every_x_and_y_for_z(params[1], params[2], params[3], beep_time, refresh_rate):
                return check_options()
            beep(beep_time)
            time.sleep(2)
            clear_display()

        elif params[0] == "tabata":
            if not down_timer(10, refresh_rate):
                return check_options()
            beep(beep_time)
            if not every_x_and_y_for_z(20, 10, 8, beep_time, refresh_rate):
                return check_options()
            beep(beep_time)
            time.sleep(2)
            clear_display()

    except IndexError:
        marquee_once("0000    ")
    except ValueError:
        beep(beep_time)
        marquee_once("1111    ")

while True:
    check_options()
    read_input()
    time.sleep(1)
