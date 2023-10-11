# What is Recursion?
# Recursion is a method of solving problems that involves breaking a problem down into smaller and smaller sub-problems until you get to a small enough problem that it can be solved trivially. Usually recursion involves a function calling itself. While it may not seem like much on the surface, recursion allows us to write elegant solutions to problems that may otherwise be very difficult to program.

# Example 1: Factorial

def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1 = 120


# print(factorial(n=5))

# Fibonacci Series

def fibonacci(n):
    if n == 0 or n == 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))
