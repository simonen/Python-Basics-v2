number = input()

max_number = -100000

while number != "Stop":
    if int(number) > max_number:
        max_number = int(number)
    number = input()

print(max_number)