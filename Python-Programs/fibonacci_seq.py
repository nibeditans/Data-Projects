# Fibonacci Sequence
def fibonacci(n):
    """

    :param n: integer
    :return: F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

number = int(input("Enter the number: "))
print("Fibonacci of number:", fibonacci(number))
