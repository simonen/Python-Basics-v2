start_int = int(input())
end_int = int(input())
magic_number = int(input())

combination = 0
is_End = False
for x in range(start_int, end_int + 1):
    for y in range(start_int, end_int + 1):
        combination += 1
        if x + y == magic_number:
            print(f"Combination N:{combination} ({x} + {y} = {magic_number})")
            is_End = True
            break
    if is_End:
        break
else:
    print(f"{combination} combinations - neither equals {magic_number}")
