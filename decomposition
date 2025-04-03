from karel.stanfordkarel import *

def main():
    move()
    # until the maze is solved, walk forwards when possible. else, check left and right, and choose clear path
    while front_is_clear() or right_is_clear() or left_is_clear():
        walk_forwards_when_possible()
        check_choose_direction()
    
#when the front is clear, keep going
def walk_forwards_when_possible():
    while front_is_clear():
        move()

#if the front is not clear, check which way to turn
def check_choose_direction():
    #making sure maze isn't solved
    if right_is_clear() or left_is_clear():
        #checking what is clear and turning
        if left_is_clear():
            turn_left()
        else:
            turn_right()

#turning right is written as a series of turning left thrice due to karel's limited inbuilt functions
def turn_right():
    for i in range(3):
        turn_left()
    

if __name__ == '__main__':
    main()
