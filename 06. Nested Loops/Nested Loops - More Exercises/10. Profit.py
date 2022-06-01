one_lev = int(input())
two_lev = int(input())
five_lev = int(input())
summ = int(input())

for a in range(0, one_lev + 1):
    for b in range(0, two_lev + 1):
        for c in range(0, five_lev + 1):
            if (a + b * 2 + 5 * c) == summ:
                print(f"{a} * 1 lv. + {b} * 2 lv. + {c} * 5 lv. = {summ} lv.")


