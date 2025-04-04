from karel.stanfordkarel import *

def main():
    #code runs as until all beepers are cleared
    while beepers_present():
        # keeps moving forwards and collecting beepers until all in the line are collected
        forwards_collecting_beepers()
        # go left and collect any beepers if present
        turn_left()
        move()
        # if no beepers are present on the left, go right instead
        if no_beepers_present():
            go_back()
            move()

# continues moving and collecting beepers until all consecutive beepers are cleared
def forwards_collecting_beepers():
    while beepers_present():
        pick_beeper()
        move()
    # go back to previous position when extra move has been made (and beeper not found)
    undo()

# go back, means going to the previous position (not orientation)
def go_back():
    turn_around()
    move()

# undo means going back to the previous position and orientation
def undo():
    go_back()
    turn_around()

# turning around is simply facing the opposite direction by turning left twice (Karel has limited functions)
def turn_around():
    for i in range(2):
        turn_left()

# turning right is done by turning left thrice (due to karel's limited functions)
def turn_right():
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    main()
