p1_start = int(input())
p2_start = int(input())
p1_diff = int(input())
p2_diff = int(input())

p1_end = p1_start + p1_diff
p2_end = p2_start + p2_diff
primes = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

for p1 in range(p1_start, p1_end + 1):
    if p1 in primes:
        for p2 in range(p2_start, p2_end + 1):
            if p2 in primes:
                print(f"{p1}{p2}")
