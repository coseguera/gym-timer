import time

# Import all board pins.
import board
import digitalio

# Create a buzzer interface
buzz = digitalio.DigitalInOut(board.GP20)
buzz.direction = digitalio.Direction.OUTPUT

# Create a led interface
led = digitalio.DigitalInOut(board.GP28)
led.direction = digitalio.Direction.OUTPUT

def beep(seconds):
    buzz.value = True
    led.value = True
    time.sleep(seconds)
    buzz.value = False
    led.value = False
