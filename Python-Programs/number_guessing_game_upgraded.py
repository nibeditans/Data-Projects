import random

play_again = 'yes'

while play_again == 'yes':
    # generate a random number between 1 and 100
    number = random.randint(1, 100)

    # set the number of guesses allowed to 10
    num_guesses_allowed = 10

    # ask the user to guess the number
    print("Guess the number between 1 and 100.")
    print("Before playing remember that you have only", num_guesses_allowed, "guesses. \nPlay well Dude:)")
    guess = int(input("Enter your guess: "))

    # keep track of the number of guesses
    num_guesses = 1

    # check if the user's guess is correct
    while guess != number and num_guesses < num_guesses_allowed:
        if guess < number:
            print("Too low! \nNow you have only", num_guesses_allowed - num_guesses, "guesses left.")
        else:
            print("Too high! \nNow you have only", num_guesses_allowed - num_guesses, "guesses left.")
        guess = int(input("Enter your guess: "))
        num_guesses += 1

    # if the user's guess is correct, congratulate them and tell them how many guesses it took
    if guess == number:
        print("Congratulations, you guessed the number in", num_guesses, "guesses!")
    else:
        print("\nGame over:( \nOops! You couldn't guess the number in",
              num_guesses_allowed, "guesses. \nBy the way the number was", number, ".")

    # ask the user if they want to play again
    play_again = input("Do you want to play again? Enter 'yes' or 'no': ").lower()

print("Okay! Thanks for playing!")
