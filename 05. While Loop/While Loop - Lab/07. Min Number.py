number = input()

min_number = 100000

while number != "Stop":
    if int(number) < min_number:
        min_number = int(number)
    number = input()

print(min_number)