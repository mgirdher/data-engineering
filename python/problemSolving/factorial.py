import time

print("hi")
def factorial_head_recursion(n):
    """
    Calculates factorial of a number using head recursion
    n (int): Input number
    return n!(int): Factorial of number
    """
    if n==0:
        return 1
    if n==1:
        return 1
    return n*factorial_head_recursion(n-1)

def factorial_tail_recursion(n,a):
    """
        Calculates factorial of a number using tail recursion
        n (int): Input number
        a(int) :integer to store last value
        return n!(int): Factorial of number
        """
    if (n == 0):
        return a
    return factorial_tail_recursion(n - 1, n * a)

# A wrapper over factTR
def fact(n):
    return factorial_tail_recursion(n, 1)

def factorial_iteration(n):
    """
        Calculates factorial of a number using while loop
        n (int): Input number
        return n!(int): Factorial of number
        """

    fact=1
    while(n>0):
        fact=fact*n
        n-=1
    return fact

