# An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
# Define a function that checks if a given number is an Armstrong number.

def is_armstrong_number(number):
    return number == sum(int(digit) ** len(str(number)) for digit in str(number))