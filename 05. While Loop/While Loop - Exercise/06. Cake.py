cake_width = int(input())
cake_length = int(input())

total_portions = cake_width * cake_length

while total_portions > 0:
    portions_taken = input()
    if portions_taken == "STOP":
        break
    total_portions -= int(portions_taken)

if total_portions >= 0:
    print(f"{total_portions} pieces are left.")
elif total_portions < 0:
    print(f"No more cake left! You need {abs(total_portions)} pieces more.")