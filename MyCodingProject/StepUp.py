"""
File: StepUp.py
Name: Vincent Lo
------------------------
This file shows Karel picking up 
the beeper at Street 1 Avenue 2,
putting it onto Street 2 Avenue 4.
Karel will be facing East at Street
2 Avenue 5 at the end of this program.
"""

from karel.stanfordkarel import *


def trun_right():
    turn_left()
    turn_left()
    turn_left()


def put_99_beepers():
    for i in range(99):
        put_beeper()


def main():
    move()
    pick_beeper()
    turn_left()
    move()
    trun_right()
    move()
    move()
    put_99_beepers()
    move()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
