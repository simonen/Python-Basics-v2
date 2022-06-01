first_time = int(input())
second_time = int(input())
third_time = int(input())

seconds_total = first_time + second_time + third_time

minutes = seconds_total // 60
seconds_remaining = seconds_total - 60 * minutes
# seconds_left = seconds_total % 60

if seconds_remaining < 10:
    print(f"{minutes}:0{seconds_remaining}")
else:
    print(f"{minutes}:{seconds_remaining}")
