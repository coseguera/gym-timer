# Import all board pins.
import board
import busio

# Import the HT16K33 LED segment module.
from adafruit_ht16k33 import segments

# Create the I2C interface.
i2c = busio.I2C(scl=board.GP27, sda=board.GP26)

# Create the LED segment class.
display = segments.Seg7x4(i2c)

# Clear the display.
display.fill(0)

prev_display = -1

def set_display(seconds):
    global prev_display
    if prev_display == seconds:
        return

    minutes = int(seconds / 60)
    seconds = int(seconds % 60)
    display.print(f'{minutes:02d}' + ':' + f'{seconds:02d}')
    display.colon = seconds % 2
    prev_display = seconds

def set_display_individual(a, b, colon, c, d):
    display[0] = a
    display[1] = b
    display.colon = colon
    display[2] = c
    display[3] = d

def marquee_once(text):
    display.marquee(text, 0.1, False)

def clear_display():
    display.fill(0)