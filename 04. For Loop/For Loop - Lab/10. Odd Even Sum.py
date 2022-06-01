n = int(input())

even_sum = 0
odd_sum = 0

for i in range(1, n + 1):
    number = int(input())
    if i % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

difference = abs(even_sum - odd_sum)

if difference == 0:
    print(f"Yes")
    print(f"Sum = {even_sum}")
else:
    print(f"No")
    print(f"Diff = {difference}")