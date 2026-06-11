# The task is to define a function that takes a string as input and returns a new string with all the vowels removed.

# Solution 1 - using regular expressions
import re
def disemvowel(string_):
    return re.sub(r'[aeiou]+', '', string_, flags=re.IGNORECASE)


# Solution 2
def disemvowel(string_):
    return ''.join(c for c in string_ if c.lower() not in 'aeiou')