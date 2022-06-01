n = int(input())

sum = 0
max_number = -1000000

for i in range(1, n + 1):
    number = int(input())
    if number > max_number:
        max_number = number
    sum += number

difference = abs(2 * max_number - sum)

if max_number == sum - max_number:
    print(f"Yes")
    print(f"Sum = {max_number}")
else:
    print(f"No")
    print(f"Diff = {difference}")
