floors = int(input())
units = int(input())

for floor in range(floors, 0, -1):
    for unit in range(0, units):
        if floor == floors:
            print("L" + str(floor) + str(unit), end=' ')
        elif floor % 2 == 0:
            print(f"O{floor}{unit}", end=' ')
        else:
            print("A" + str(floor) + str(unit), end=' ')
    print()