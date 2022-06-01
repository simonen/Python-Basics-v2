number = int(input())
counter = 1
is_end = False
for row in range(1, number + 1):
    for col in range(1, row + 1):
        print(counter, end=" ")
        if counter == number:
            is_end = True
            break
        counter += 1
    if is_end:
        break
    print()
