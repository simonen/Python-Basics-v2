season = input()
distance = float(input())

income = distance

if distance <= 5000:
    if season == "Summer":
        income *= 0.90
    elif season == "Winter":
        income *= 1.05
    else:
        income *= 0.75
elif distance <= 10000:
    if season == "Summer":
        income *= 1.1
    elif season == "Winter":
        income *= 1.25
    else:
        income *= 0.95
else:
    income *= 1.45

profit = 4 * income * 0.9

print(f"{profit:.2f}")

