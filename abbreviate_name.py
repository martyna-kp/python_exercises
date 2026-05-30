#Write a function to convert a name into initials.

#The output should be two capital letters with a dot separating them.

def abbrev_name(name):
    return str(name.split(' ')[0][0]).upper() + "." + str(name.split(' ')[1][0]).upper()