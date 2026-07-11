import math

def scientific_calculator():
    print("Welcome to the Scientific Calculator!")
  
    while True:
        print("Select an operation: ")
        print("1. Addition, 2. Subtraction, 3. Multiplication, 4. Division, 5. Modulus, 6. Power,",
              "\n7. Square Root, 8. Logarithm, 9. Sine, 10. Cosine, 11. Tangent, 12. pi, 13. Exit")

        choice = input("Enter choice (1-13): ")

        if choice in ('1', '2', '3', '4', '5', '6'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", num1 + num2)

            elif choice == '2':
                print(num1, "-", num2, "=", num1 - num2)

            elif choice == '3':
                print(num1, "*", num2, "=", num1 * num2)

            elif choice == '4':
                print(num1, "/", num2, "=", num1 / num2)

            elif choice == '5':
                print(num1, "%", num2, "=", num1 % num2)

            elif choice == '6':
                print(num1, "**", num2, "=", num1 ** num2)

        elif choice == '7':
            num = float(input("Enter a number: "))
            print("Square root of", num, "is", math.sqrt(num))

        elif choice == '8':
            num = float(input("Enter a number: "))
            print("Log(base 2) of", num, "is", math.log2(num))

        elif choice == '9':
            num = float(input("Enter a number: "))
            print("Sin of", num, "is", math.sin(num))

        elif choice == '10':
            num = float(input("Enter a number: "))
            print("Cos of", num, "is", math.cos(num))

        elif choice == '11':
            num = float(input("Enter a number: "))
            print("Tan of", num, "is", math.tan(num))

        elif choice == '12':
            print("pi = ", math.pi)

        elif choice == '13':
            print("Exiting the program")
            break

        else:
            print("Invalid input. Please try again.")

scientific_calculator()
