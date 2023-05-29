import random

winning_moves = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

def play():
    moves = ["rock", "paper", "scissors"]
    player_choice = input("Enter your move(rock, paper, scissors): ").lower().strip()
    computer_choice = moves[random.randint(0, 2)]

    if player_choice not in moves:
        print("Invalid input, please try again.")
        return 0

    print(f"You chose {player_choice}, computer chose {computer_choice}.")

    if player_choice == computer_choice:
        print("It's a draw.")
    elif winning_moves[player_choice] == computer_choice:
        print("You win!")
    else:
        print("You lose.")

play()