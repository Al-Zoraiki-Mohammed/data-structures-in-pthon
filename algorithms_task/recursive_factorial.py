""" Recursive factorial implementation
"""


def factorial(num: int):
    """Calculate factorial of the number"""

    if not isinstance(num, int) or num < 0:
        raise Exception(f"Type Error: number must be positive integer")
    
    if num == 0:
        return 1
    
    return num * factorial(num-1)


if __name__ == "__main__":
    print(factorial(5))
    print(factorial(1))
    print(factorial(0))
    print(factorial(5.5))  # Exception will be raised
    print(factorial(-5))   # Exception will be raised
    print(factorial('a'))  # Exception will be raised
