n = int(input())

current_pair = 0
previous_pair = 0
max_diff = 0
difference = 0

for i in range(n):
    current_pair = int(input()) + int(input())
    if i > 0:
        difference = abs(current_pair - previous_pair)
    if difference > max_diff:
        max_diff = difference
    previous_pair = current_pair

if max_diff == 0:
    print(f"Yes, value={current_pair}")
else:
    print(f"No, maxdiff={max_diff}")
