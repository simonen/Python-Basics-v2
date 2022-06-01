budget = float(input())
gpus = int(input())
cpus = int(input())
ram_sticks = int(input())

total_cost = gpus * 250 * (1 + cpus * 0.35 + ram_sticks * 0.1)

if gpus > cpus:
    total_cost *= 0.85

difference = abs(budget - total_cost)

if budget >= total_cost:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")