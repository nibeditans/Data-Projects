# Health Management System
# There are 3 clients - Nibe, Dita and Nibedita


# Total 6 files
# Write a function that takes as input client name when executed
# One more function to retrieve exercise or food for any client


# So, here is the Code Dude
import datetime

def gettime():
    return datetime.datetime.now()

def take(n):
    if n == 1:
        i = int(input("Enter 1 for excersise & 2 for food: "))
      
        if i == 1:
            value = input("Type here\n")
            with open("Nibe-ex.txt", "a") as ns:
                ns.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
        elif i == 2:
            value = input("Type here\n")
            with open("Nibe-food.txt", "a") as ns:
                ns.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
    elif n == 2:
        i = int(input("Enter 1 for excersise & 2 for food: "))
        if i == 1:
            value = input("Type here\n")
            with open("Dita-ex.txt", "a") as ns:
                ns.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
        elif i == 2:
            value = input("Type here\n")
            with open("Dita-food.txt", "a") as ns:
                ns.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
    elif n == 3:
        i = int(input("Enter 1 for excersise & 2 for food: "))
        if i == 1:
            value = input("Type here\n")
            with open("Nibedita-ex.txt", "a") as ns:
                ns.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
        elif i == 2:
            value = input("Type here\n")
            with open("Nibedita-food.txt", "a") as ns:
                ns.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
    else:
        print("Please enter valid input (1(Nibe),2(Dita),3(Nibedita)")

def retrieve(n):
    if n == 1:
        i = int(input("Enter 1 for excersise & 2 for food: "))
        if i== 1:
            with open("Nibe-ex.txt") as ns:
                for k in ns:
                    print(k, end="")
        elif i == 2:
            with open("Nibe-food.txt") as ns:
                for k in ns:
                    print(k, end="")
    elif n == 2:
        i = int(input("Enter 1 for excersise & 2 for food: "))
        if i == 1:
            with open("Dita-ex.txt") as ns:
                for k in ns:
                    print(k, end="")
        elif i == 2:
            with open("Dita-food.txt") as ns:
                for k in ns:
                    print(k, end="")
    elif n == 3:
        i = int(input("Enter 1 for excersise & 2 for food: "))
        if i == 1:
            with open("Nibedita-ex.txt") as ns:
                for k in ns:
                    print(k, end="")
        elif i == 2:
            with open("Nibedita-food.txt") as ns:
                for k in ns:
                    print(k, end="")
    else:
        print("Please enter valid input (Nibe, Dita and Nibedita)")


print("Health Management System! ")
a = int(input("Press 1 for log the value & 2 for retrieve the value: "))

if a == 1:
    b = int(input("Press 1 for Nibe, 2 for Dita & 3 for Nibedita: "))
    take(b)
else:
    b = int(input("Press 1 for Nibe, 2 for Dita & 3 for Nibedita: "))
    retrieve(b)
