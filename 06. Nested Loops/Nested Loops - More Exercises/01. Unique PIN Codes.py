first = int(input())
second = int(input())
third = int(input())

primes = [2, 3, 5, 7]

for f in range(2, first + 1):
    if f % 2 == 0:
        for s in range(2, second + 1):
            if s in primes:
                for t in range(2, third + 1):
                    if t % 2 == 0:
                        print(f"{f} {s} {t}")

