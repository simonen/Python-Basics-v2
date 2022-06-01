turns = int(input())

points = 0
invalid_numbers = 0
to_nine = 0
to_nineteen = 0
to_twenty_nine = 0
to_thirty_nine = 0
to_fifty = 0

for turn in range(turns):
    number = int(input())
    if number < 0 or number > 50:
        points *= 0.5
        invalid_numbers += 1
    elif 0 <= number <= 9:
        points += number * 0.2
        to_nine += 1
    elif number <= 19:
        points += number * 0.3
        to_nineteen += 1
    elif number <= 29:
        points += number * 0.4
        to_twenty_nine += 1
    elif number <= 39:
        to_thirty_nine += 1
        points += 50
    elif number <= 50:
        to_fifty += 1
        points += 100

invalid_p = invalid_numbers / turns * 100
to_nine_p = to_nine / turns * 100
to_nineteen_p = to_nineteen / turns * 100
to_twenty_nine_p = to_twenty_nine / turns * 100
to_thirty_nine_p = to_thirty_nine / turns * 100
to_fifty_p = to_fifty / turns * 100

print(f"{points:.2f}")
print(f"From 0 to 9: {to_nine_p:.2f}%")
print(f"From 10 to 19: {to_nineteen_p:.2f}%")
print(f"From 20 to 29: {to_twenty_nine_p:.2f}%")
print(f"From 30 to 39: {to_thirty_nine_p:.2f}%")
print(f"From 40 to 50: {to_fifty_p:.2f}%")
print(f"Invalid numbers: {invalid_p:.2f}%")
