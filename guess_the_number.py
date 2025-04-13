import random

print("I'm thinking of a number between 1 and 99!")

number = random.randint(1,99) # the program thinks of a number
chance = int(input("How many guesses do you want? ")) # can be changed!
current_chance = chance-1 # no of chances left!

print("You have",chance, "chances to guess the number!")


def main():
  # purpose: conduct game till completion
    global chance
  # stops game after given number of chances
    for i in range(chance):
        play_game()
    print("The answer was " + str(number) + "!")


def give_instructions():
    print("I'm thinking of a number between 1 and 99!")
    print("You have",chance, "chances to guess the number!")


def play_game():
    global current_chance
  # the user enters their guess
    guess = int(input("Enter your guess! "))
  
    if guess == number:
        print("You guessed it right! The number was "+ str(number) + "!")
        exit()
    elif number > guess:
        print("Your guess was too low! You have " + str(current_chance) + " chances left!")
    else:
        print("Your guess was too high! You have " + str(current_chance) + " chances left!")
    current_chance -= 1 # this ensures the turn is accounted for, no. of chances left decreases by 1

if __name__ == "__main__":
    main()
