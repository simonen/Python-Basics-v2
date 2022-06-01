n = int(input())

total_count = 2 * n
left_sum = 0
right_sum = 0

for i in range(1, total_count + 1):
    if i <= total_count / 2:
        number = int(input())
        left_sum += number
    else:
        number = int(input())
        right_sum += number

difference = abs(left_sum - right_sum)

if right_sum == left_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {difference}")
