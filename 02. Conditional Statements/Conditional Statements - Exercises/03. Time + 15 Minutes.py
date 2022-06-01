hours = int(input())
minutes = int(input())

total_minutes = hours * 60 + minutes + 15

new_hour = total_minutes // 60
minutes_remaining = total_minutes % 60

if new_hour > 23:
    new_hour = 0
if minutes_remaining < 10:
    print(f"{new_hour}:0{minutes_remaining}")
else:
    print(f"{new_hour}:{minutes_remaining}")

# hours = int(input())
# minutes = int(input())
#
# minutes += 15
# hours += minutes // 60
# minutes %= 60
# if hours > 23:
#     hours %= 24
# print(f"{hours}:{minutes}")
