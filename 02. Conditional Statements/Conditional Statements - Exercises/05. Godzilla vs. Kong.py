budget = float(input())
extras = int(input())
costume_cost = float(input())

if extras > 150:
    costume_cost *= 0.9

decors = budget * 10 / 100
total_cost = extras * costume_cost + decors
difference = abs(budget - total_cost)

if budget >= total_cost:
    print(f"Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
else:
    print(f"Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")