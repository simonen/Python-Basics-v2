actor = input()
total_points = float(input())
judges = int(input())

difference = 0
for i in range(1, judges + 1):
    judge = input()
    points = float(input())
    total_points += len(judge) * points / 2
    if total_points >= 1250.5:
        print(f"Congratulations, {actor} got a nominee for leading role with {total_points:.1f}!")
        break
    difference = 1250.5 - total_points
else:
    print(f"Sorry, {actor} you need {difference:.1f} more!")