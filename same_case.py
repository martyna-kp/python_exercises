# Write a function that will check if two given characters are the same case.

# If either of the characters is not a letter, return -1
# If both characters are the same case, return 1
# If both characters are letters, but not the same case, return 0

def same_case(a, b): 
    if not (a.isalpha() and b.isalpha()):
        return -1
    elif ((a.islower() and b.islower()) or (a.isupper() and b.isupper())):
          return 1
    else:
          return 0