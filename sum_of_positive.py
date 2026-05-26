# You get an array of numbers, return the sum of all of the positives ones.

def positive_sum(arr):
    return sum(num for num in arr if num > 0)