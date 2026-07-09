# Task
# Implement a way to determine whether a given number is perfect, abundant or deficient.

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    divisors = []
    for i in range (1,number+1):
        if number % i == 0 and i != number:
            divisors.append(i)
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    if sum(divisors) == number:
        return "perfect"
    if sum(divisors) > number:
        return "abundant"
    if sum(divisors) < number:
        return "deficient"