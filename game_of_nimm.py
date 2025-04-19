import random

stones = 20
player = 1
human_plays = 1

def main():
    global stones
    global player
    global human_plays
    human_plays = choose_player(human_plays)
    while stones > 0:
        print("There are " + str(stones) + " stones left.")
        stones = no_of_stones(stones)
        player = change_turn(player)
        print()
    finish_game()

# allows user to choose whether they want to go first or second
def choose_player(x):
    number = int(input("Would you like to be player 1 or player 2? "))
    while number not in (1,2):
        number = int(input("Please enter 1 or 2: "))
    x = number
    return x

# alternating players
def change_turn(a):
    if a == 1:
        a = 2
    else:
        a = 1
    return a

# account of number of stones left
def no_of_stones(x):
        global player
        if player == human_plays:
            stones_removed = int(input("Player " + str(player) + " would you like to remove 1 or 2 stones? "))
            while stones_removed not in (1,2):
                stones_removed = int(input("Please enter 1 or 2: "))
        else:
            stones_removed = random.randint(1,2)
            print("Player " + str(player) + " would you like to remove 1 or 2 stones? " + str(stones_removed))
        x -= stones_removed
        return x

# tell user that the game is over
def finish_game():
    global player
    print("Player " + str(player) + " wins!")

main()
