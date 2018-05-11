# Chapter 16 Practice Questions

# 1. Why can't a brute-force attack be used against a simple substitution
# cipher, even with a powerful supercomputer?
# Hint: Check page 208
from math import factorial  # Don't do this - imports should be at the top of the file
numKeys = factorial(26)
print(numKeys)

# 2. What does the spam variable contain after running this code?
spam = [4, 6, 2, 8]
spam.sort()
print(spam)

# 3. What is a wrapper function?
# Hint: Check page 213


def calculator(num1, num2, mode):
    if mode == "add":
        return num1 + num2
    elif mode == "subtract":
        return num1 - num2
    return None


def addition(num1, num2):
    return calculator(num1, num2, "add")


def subtraction(num1, num2):
    return calculator(num1, num2, "subtract")


print(addition(3, 4))
print(subtraction(2, 1))

# 4. What does 'hello'.islower() evaluate to?
print('hello'.islower())

# 5. What does 'HELLO 123'.isupper() evaluate to?
print('HELLO 123'.isupper())

# 6. What does '123'.islower() evaluate to?
print('123'.islower())
