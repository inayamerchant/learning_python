stones = 20
player = 1

def main():
    global stones
    global player
    while stones > 0:
        print("There are " + str(stones) + " stones left.")
        stones = no_of_stones(stones)
        player = change_turn(player)
        print()
    finish_game()


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
        stones_removed = int(input("Player " + str(player) + " would you like to remove 1 or 2 stones? "))
        while stones_removed not in (1,2):
            stones_removed = int(input("Please enter 1 or 2: "))
        x -= stones_removed
        return x

# tell user that the game is over
def finish_game():
    global player
    print("Player " + str(player) + " wins!")

main()
