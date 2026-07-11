n = 19
number_of_guesses = 1

print("Number of guesses is limited to only 7 times: ")

while number_of_guesses <= 7:
    guess_number = int(input("Guess the number :\n"))
    if guess_number < 19:
        print("you entered a smaller number please guess a greater number.\n")
    elif guess_number > 19:
        print("you entered a bigger number please guess a smaller number.\n ")
    else:
        print("Congrats Dude! You did it.")
        print(number_of_guesses,"guesses you took to finish.")
        break
    print(7 - number_of_guesses,"guesses left")
    number_of_guesses = number_of_guesses + 1

if number_of_guesses > 7:
    print("Game Over:)\nOops! Sorry Dude, you couldn't guess the number: ")
