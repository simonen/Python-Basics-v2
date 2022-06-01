n = int(input())
counter = 0
total_sum = 0
average = 0
while counter < n:
    number = int(input())
    total_sum += number
    average = total_sum / n
    counter += 1
print(f"{average:.2f}")