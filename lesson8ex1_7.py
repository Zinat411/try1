total = 0
def fibonacci(n):
    """Return the nth fibonacci number.

    >>> fibonacci(11)
    89
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

total = fibonacci(11)
print(total)
