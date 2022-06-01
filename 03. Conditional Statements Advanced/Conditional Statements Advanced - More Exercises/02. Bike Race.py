junior_bikers = int(input())
senior_bikers = int(input())
terrain = input()

income = 0
price = 0

if terrain == "trail":
    income = junior_bikers * 5.5 + senior_bikers * 7
elif terrain == "downhill":
    income = junior_bikers * 12.25 + senior_bikers * 13.75
elif terrain == "road":
    income = junior_bikers * 20 + senior_bikers * 21.50
elif terrain == "cross-country":
    income = junior_bikers * 8 + senior_bikers * 9.5
    if junior_bikers + senior_bikers >= 50:
        income *= 0.75

profit = income * 0.95

print(f"{profit:.2f}")

