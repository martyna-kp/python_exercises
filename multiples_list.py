# Create a function with two arguments that will return a list of the first n multiples of x.

# Assume both the given number and the number of times to count will be positive numbers greater than 0.

def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    return [x * i for i in range(1, n+1, 1)]