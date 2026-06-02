# Write a function bmi that calculates body mass index (bmi = weight / height2).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"

def bmi(weight, height):
    bmi_score = weight/(height**2)
    if bmi_score <= 18.5:
        return "Underweight"
    elif bmi_score <= 25:
        return "Normal"
    elif bmi_score <= 30:
        return "Overweight"
    else:
        return "Obese"