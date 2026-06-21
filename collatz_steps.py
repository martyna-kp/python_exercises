# Implement a function that returns the number of steps needed for a positive integer to reach 1 following the Collatz rules:

# Even numbers → divide by 2
# Odd numbers → multiply by 3 and add 1

# Raise a `ValueError` for zero or negative inputs.

def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    number_of_steps = 0
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        number_of_steps += 1
    return number_of_steps
