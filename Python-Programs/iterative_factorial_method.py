# Iterative Method
def factorial_iterative(n):
    """

    :param n: integer
    :return: n * (n-1) * (n-2) * ... * 3 * 2 * 1
    """
    fac = 1
    for i in range(n):
        fac *= (i+1)
    return fac

number = int(input("Enter the number: "))
print("Factorial using Iterative method:", factorial_iterative(number))
