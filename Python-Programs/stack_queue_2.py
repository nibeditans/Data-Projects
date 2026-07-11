lis = []

# What we're going to do in the program.
print("""c = int(input('''
    1. Push Elements
    2. Pop First Elements
    3. Front Element 
    4. Last Element
    5. Display Queue
    6. Exit '''))\n""")

while True:
    num_inp = int(input("Enter the number: "))

    if num_inp == 1:
        num = input("Enter the value you want to display in the Queue: ")
        lis.append(num)
        print(lis)

    elif num_inp == 2:
        if len(lis) == 0:
            print("Empty Queue.")
        else:
            del lis[0]
            print(lis)

    elif num_inp == 3:
        if len(lis) == 0:
            print("Empty Queue.")
        else:
            print("First Queue Value: ", lis[0])

    elif num_inp == 4:
        if len(lis) == 0:
            print("Empty Queue.")
        else:
            print("Last Queue Value: ", lis[-1])

    elif num_inp == 5:
        print("Display Queue: ", lis)

    elif num_inp == 6:
        break

    else:
        print("Not acceptable! [You should check the instructions above]")
