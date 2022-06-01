import sys

fruit = input()
day = input()
quantity = float(input())

price = 0
is_fruit_valid = True
is_day_valid = True

if fruit == "banana":
    price = 2.50
    if day == "Saturday" or day == "Sunday":
        price = 2.70
elif fruit == "apple":
    price = 1.20
    if day == "Saturday" or day == "Sunday":
        price = 1.25
elif fruit == "orange":
    price = 0.85
    if day == "Saturday" or day == "Sunday":
        price = 0.9
elif fruit == "grapefruit":
    price = 1.45
    if day == "Saturday" or day == "Sunday":
        price = 1.6
elif fruit == "kiwi":
    price = 2.70
    if day == "Saturday" or day == "Sunday":
        price = 3
elif fruit == "pineapple":
    price = 5.50
    if day == "Saturday" or day == "Sunday":
        price = 5.6
elif fruit == "grapes":
    price = 3.85
    if day == "Saturday" or day == "Sunday":
        price = 4.2
else:
    is_fruit_valid = False

cost = price * quantity

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or \
        day == "Saturday" or day == "Sunday":
    pass
else:
    is_day_valid = False

if is_day_valid and is_fruit_valid:
    print(f"{cost:.2f}")
else:
    print("error")
