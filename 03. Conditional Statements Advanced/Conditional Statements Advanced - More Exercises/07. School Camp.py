season = input()
group_type = input()
students = int(input())
nights = int(input())
price = 0
sport = ''

if season == "Winter":
    if group_type == "mixed":
        sport = "Ski"
        price = 10
    else:
        price = 9.6
        if group_type == "boys":
            sport = "Judo"
        elif group_type == "girls":
            sport = "Gymnastics"
elif season == "Spring":
    if group_type == "mixed":
        sport = "Cycling"
        price = 9.5
    else:
        price = 7.2
        if group_type == "boys":
            sport = "Tennis"
        elif group_type == "girls":
            sport = "Athletics"
elif season == "Summer":
    if group_type == "mixed":
        sport = "Swimming"
        price = 20
    else:
        price = 15
        if group_type == "boys":
            sport = "Football"
        elif group_type == "girls":
            sport = "Volleyball"

cost = students * price * nights

if 10 <= students < 20:
    cost *= 0.95
elif 20 <= students < 50:
    cost *= 0.85
elif students >= 50:
    cost *= 0.5

print(f"{sport} {cost:.2f} lv.")
