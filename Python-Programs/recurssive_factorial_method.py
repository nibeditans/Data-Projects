# Recursion
def factorial_recursive(n):
    """

    Returns the factorial of a number using recursion.

    Parameters:
    -----------
    n : int
        The number whose factorial is to be calculated.

    Returns:
    --------
    int
        The factorial of the input number `n`.
    """
    
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

number = int(input("Enter the number: "))
print("Factorial using Recursive method:", factorial_recursive(number))
