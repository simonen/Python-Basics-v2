n = int(input())

left_sum = 0
right_sum = 0

for a in range(1, 10):
    count_a = 0
    for b in range(1, 10):
        left_sum = a + b
        if n % left_sum == 0:
            count_a = 1
        else:
            continue
        for c in range(1, 10):
            for d in range(1, 10):
                right_sum = c + d
                if left_sum == right_sum and count_a == 1:
                    print(f"{a}{b}{c}{d}", end=" ")

