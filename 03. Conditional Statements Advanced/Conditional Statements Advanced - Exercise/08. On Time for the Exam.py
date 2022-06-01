hour_of_exam = int(input())
minute_of_exam = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

total_minutes_exam = hour_of_exam * 60 + minute_of_exam
total_minutes_arrival = hour_of_arrival * 60 + minute_of_arrival
difference = abs(total_minutes_exam - total_minutes_arrival)

if total_minutes_exam == total_minutes_arrival:
    print(f"On time")
elif total_minutes_exam < total_minutes_arrival:
    print(f"Late")
    if difference >= 60:
        print(f"{difference // 60}:{(difference % 60):02d} hours after the start")
    else:
        print(f"{difference} minutes after the start")
elif total_minutes_exam - total_minutes_arrival > 30:
    print(f"Early")
    if difference >= 60:
        print(f"{difference // 60}:{(difference % 60):02d} hours before the start")
    else:
        print(f"{difference} minutes before the start")
elif total_minutes_exam - total_minutes_arrival <= 30:
    print(f"On time")
    if difference >= 60:
        print(f"{difference // 60}:{(difference % 60):02d} hours before the start")
    else:
        print(f"{difference} minutes before the start")