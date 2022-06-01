days_off = int(input())

work_days = 365 - days_off
play_time = work_days * 63 + days_off * 127
difference = abs(30000 - play_time)

hours_more = difference // 60
minutes_more = difference % 60

if play_time > 30000:
    print("Tom will run away")
    print(f"{hours_more} hours and {minutes_more} minutes more for play")
elif play_time < 30000:
    print("Tom sleeps well")
    print(f"{hours_more} hours and {minutes_more} minutes less for play")
