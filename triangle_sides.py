# Determine if a triangle is equilateral, isosceles, or scalene.

def istriangle(sides):
    a, b, c = sides
    return a + b >= c and b + c >= a and a + c >= b and a > 0 and b > 0 and c > 0

def equilateral(sides):
    return len(set(sides)) == 1 and istriangle(sides)

def isosceles(sides):
    return len(set(sides)) <= 2 and istriangle(sides)

def scalene(sides):
    return len(set(sides)) == 3 and istriangle(sides)