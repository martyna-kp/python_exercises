# Write a function that removes the spaces from the string, then return the resultant string.

# Solution 1
def no_space(x):
    return x.replace(" ","")

# Solution 2
def no_space(x):
    return "".join(x.split())
