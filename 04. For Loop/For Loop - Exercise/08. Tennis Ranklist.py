import math

tournaments = int(input())
starting_points = int(input())

stage = ''
wins = 0
total_points = starting_points

for i in range(1, tournaments + 1):
    stage = input()
    if stage == "W":
        total_points += 2000
        wins += 1
    elif stage == "F":
        total_points += 1200
    elif stage == "SF":
        total_points += 720

average = (total_points - starting_points) / tournaments
wins_p = wins / tournaments * 100

print(f"Final points: {total_points}")
print(f"Average points: {math.floor(average):.0f}")
print(f"{wins_p:.2f}%")
