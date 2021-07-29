# gym-timer
A gym timer that fits in a small tin can

## Instructions
### To load the code to your board
1. Get CircuitPython 7+ on your board. You can find your board [here](https://circuitpython.org/downloads).
1. Get the CircuitPython 7+ libraries from [here](https://circuitpython.org/libraries).
1. Copy `adafruid_bus_service` and `adafruit_ht16k33` to the lib folder in your board.
1. Copy all the code from `src/gym-timer` to the root folder of your board.

### To send commands to the timer on Mac/Linux
1. Copy `src/gym-timer.sh` to your machine 
1. Make sure the file is executable by doing `chmod +x ./gym-timer.sh` (or if you need to use sudo `sudo chmod +x ./gym-timer.sh`)
1. Send the command that you want to use!

    Up:
    - `./gym-timer.sh up/3` or `./gym-timer.sh up/3/seconds` counts up 3 seconds.
    - `./gym-timer.sh up/3/minutes` counts up 3 minutes.

    Down:
    - `./gym-timer.sh down/3` or `./gym-timer.sh down/3/seconds` counts down 3 seconds.
    - `./gym-timer.sh down/3/minutes` counts down 3 minutes.

    EMOM:
    - `./gym-timer.sh emom/3` does an "every minute over minute" for 3 minutes.

    Every X time for Y reps:
    - `./gym-timer.sh every/3/seconds/for/5` counts up 3 seconds 5 times.
    - `./gym-timer.sh every/3/minutes/for/5` counts up 3 minutes 5 times.

    Tabata:
    - `./gym-timer.sh tabata` does a Tabata timer.

    Every X time, then Y time for Z reps (adjustable Tabata):
    - `./gym-timer.sh every/10/seconds/and/15/seconds/for/5` counts up 10 seconds and immediately counts up 15 seconds for 5 times.
    - `./gym-timer.sh every/10/seconds/and/15/minutes/for/5` counts up 10 seconds and immediately counts up 15 minutes for 5 times.
    - `./gym-timer.sh every/10/minutes/and/15/seconds/for/5` counts up 10 minutes and immediately counts up 15 seconds for 5 times.
    - `./gym-timer.sh every/10/minutes/and/15/minutes/for/5` counts up 10 minutes and immediately counts up 15 minutes for 5 times.