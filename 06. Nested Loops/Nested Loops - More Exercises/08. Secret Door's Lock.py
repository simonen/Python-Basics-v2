f_upper = int(input())
s_upper = int(input())
t_upper = int(input())

primes = [2, 3, 5, 7]

for f in range(1, f_upper + 1):
    if f % 2 == 0:
        pass
    else:
        continue
    for s in range(1, s_upper + 1):
        if s in primes:
            pass
        else:
            continue
        for t in range(1, t_upper + 1):
            if t % 2 == 0:
                print(f"{f} {s} {t}")


# for f in range(1, f_upper + 1):
#     if f % 2 == 0:
#         for s in range(1, s_upper + 1):
#             if s in primes:
#                 for t in range(1, t_upper + 1):
#                     if t % 2 == 0:
#                         print(f"{f} {s} {t}")
