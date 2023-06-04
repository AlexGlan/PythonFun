from random import randint
from sys import argv
from drawings import dice

def roll():
    # Get the number of dice from command line
    if len(argv) < 2:
        number_of_dice = 1
    else:
        number_of_dice = int(argv[1])
    
    def roll_dice():
            """Roll the dice for the specified number of times"""
            counter = 0
            while(counter < number_of_dice):
                counter += 1
                print_dice()

    def print_dice():
            """Print the visual representation of a random dice roll"""
            random_number = randint(1, 6)
            result.append(random_number)
            print("\n".join(dice[random_number]))
    
    # Main game loop
    user_input = ""
    result = []
    while(user_input != "q"):
        roll_dice()

        # Print the result of the dice roll
        if len(result) == 1:
            print(f"You rolled {result[0]}.")
        else:
            print(f"You rolled {sum(result)}, {result}.")

        result.clear()
        user_input = input("Press any type key to keep rolling (q to quit). ").lower().strip()

roll()