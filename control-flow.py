from karel.stanfordkarel import *

# karel checks if it needs to cross a hurdle, or simply move
def main():
    for i in range(8):
        if front_is_blocked():
            cross_hurdle()
        else:
            move()

""" crossing a hurdle:
    - face the right direction
    - ascend hurdle
    - move and change direction
    - descend hurdle
    - move to initial position
"""
def cross_hurdle():
    turn_left()
    ascend_hurdle()
    turn_right()
    move()
    turn_right()
    move()
    descend_hurdle()
    turn_left()

# ascending the hurdle
def ascend_hurdle():
    while right_is_blocked():
        move()

# descending the hurdle
def descend_hurdle():
    while front_is_clear():
        move()

#turn right = turn left thrice
def turn_right():
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    main()
