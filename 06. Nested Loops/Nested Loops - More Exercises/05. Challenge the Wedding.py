men = int(input())
women = int(input())
tables = int(input())

is_Tables = True
for m in range(1, men + 1):
    for w in range(1, women + 1):
        print(f"({m} <-> {w})", end=" ")
        tables -= 1
        if tables == 0:
            is_Tables = False
            break
    if not is_Tables:
        break
