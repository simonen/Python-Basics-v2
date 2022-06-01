start_int = int(input())
end_int = int(input())
magic_number = int(input())

count = 0
combination = 0
for x in range(start_int, end_int + 1):
    for y in range(start_int, end_int + 1):
        count += 1
        if x + y == magic_number:
            print(f"Combination N:{count} ({x} + {y} = {magic_number})")
            combination = 1
            break
    if combination == 1:
        break
if combination == 0:
    print(f"{count} combinations - neither equals {magic_number}")
