import random

print("Let's play Stone Paper Scissors!")
print("You will be playing against the computer.")
print("We'll play 7 rounds, and whoever wins more rounds will be the winner.")

play_again = "y"

while play_again.lower() == "y":
    rounds_to_play = 7
    user_score = 0
    computer_score = 0

    for round_num in range(1, rounds_to_play + 1):
        print(f"Round {round_num}:")

        # Get user's choice
        user_choice = input("Enter your choice (s for Stone, p for Paper, sc for Scissors): ").lower()
        while user_choice not in ("s", "p", "sc"):
            user_choice = input("Invalid choice. Enter your choice again (s for Stone, p for Paper, sc for Scissors): ").lower()

        # Map abbreviated input to full word
        if user_choice == "s":
            user_choice_text = "Stone"
        elif user_choice == "p":
            user_choice_text = "Paper"
        else:
            user_choice_text = "Scissors"

        # Generate computer's choice
        computer_choice = random.choice(["s", "p", "sc"])
        if computer_choice == "s":
            computer_choice_text = "Stone"
        elif computer_choice == "p":
            computer_choice_text = "Paper"
        else:
            computer_choice_text = "Scissors"

        print(f"You chose {user_choice_text}, and the computer chose {computer_choice_text}.")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == "s":
            if computer_choice == "sc":
                print("You win! Stone smashes scissors.")
                user_score += 1
            else:
                print("You lose. Paper covers stone.")
                computer_score += 1
        elif user_choice == "p":
            if computer_choice == "s":
                print("You win! Paper covers stone.")
                user_score += 1
            else:
                print("You lose. Scissors cut paper.")
                computer_score += 1
        else:
            if computer_choice == "p":
                print("You win! Scissors cut paper.")
                user_score += 1
            else:
                print("You lose. Stone smashes scissors.")
                computer_score += 1

        print(f"The score is now {user_score} (you) - {computer_score} (computer).\n")

    # Determine the winner of the game
    if user_score == computer_score:
        print("It's a tie! Nobody wins.")
    elif user_score > computer_score:
        print(f"You win the game with a score of {user_score} to {computer_score}!")
    else:
        print(f"You lose the game with a score of {computer_score} to {user_score}.")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (y/n) ")

print("Thanks for playing!")
