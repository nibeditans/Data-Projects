lis = []

# What we're gonna do in the program.
# c = int(input("""
    # 1. Push Elements:
    # 2. Pop Elements:
    # 3. Peek Element:
    # 4. Display Stack:
    # 5. Exit """))

print("See the above chat for better understanding what actually is happening!")

while True:
    num_inp = int(input("Enter the number: "))

    if num_inp == 1:
        num = input("Enter the value you want to display in the Stack: ")
        lis.append(num)
        print(lis)

    elif num_inp == 2:
        if len(lis) == 0:
            print("Empty Stack.")
        else:
            p = lis.pop()
            print(p)
            print(lis)

    elif num_inp == 3:
        if len(lis) == 0:
            print("Empty Stack.")
        else:
            print("Last Stack Value: ", lis[-1])

    elif num_inp == 4:
        print("Display Stack: ", lis)

    else:
        break
