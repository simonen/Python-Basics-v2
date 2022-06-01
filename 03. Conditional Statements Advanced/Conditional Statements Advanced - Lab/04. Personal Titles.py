age = float(input())
gender = input()
title = ""

if gender == "m":
    if age >= 16:
        title = "Mr."
    else:
        title = "Master"
elif gender == "f":
    if age >= 16:
        title = "Ms."
    else:
        title = "Miss"

print(title)

if age >= 16:
    if gender == "m":
        title = "Mr."
    elif gender == "f":
        title = "Ms."
else:
    if gender == "m":
        title = "Master"
    elif gender == "f":
        title = "Miss"
print(title)