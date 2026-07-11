import random

print("""Instructions:
Enter 'r', 'p', or 's' only. If you typed anything else other than one among them, then computer will be going 
to take advantage of it. Computer will get 1 point and you'll get 0 points. So, give your choice carefully.
""")
lis = ['Rock', 'Paper', 'Scissors']
print("Game is starting...")

while True:
    user_count = 0
    com_count = 0

    your_inp = input("\nType 'yes' to play or type anything to exit the Game: ")
    if your_inp == 'yes':
        for _ in range(1, 6):
            user_input = input("""
            r for Rock
            p for Paper
            s for Scissors:
                                """)

            your_choice = []
            
            if user_input == 'r':
                your_choice = "Rock"
            elif user_input == 'p':
                your_choice = "Paper"
            elif user_input == 's':
                your_choice = "Scissors"
            else:
                print("You're supposed to enter 'r', 'p' or 's' only. "
                      "You missed your 1 point from your chances to win and computer took advantage of it.")

            com_choice = random.choice(lis)
            
            if com_choice == your_choice:
                print("It's a draw!")
                com_count += 1
                user_count += 1
            elif (your_choice == 'Scissors' and com_choice == 'Paper') or (your_choice == 'Paper' and com_choice == 'Rock') or (your_choice == 'Rock' and com_choice == 'Scissors'):
                print("Congrats! You won this round.")
                user_count += 1
            else:
                print("Oops! Computer won this round.")
                com_count += 1

        print("\nYou got", user_count, "points and computer got", com_count, "points.")
        
        if user_count == com_count:
            print("FINAL RESULT: Match Draw! You both got the same points.")
        elif user_count > com_count:
            print("FINAL RESULT: Congrats! You won the game as you have scored more than computer.")
        else:
            print("FINAL RESULT: Oh no! Computer won the game as you have scored less than computer.")

    else:
        break
