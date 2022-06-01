flower = input()
flower_count = int(input())
budget = int(input())

price = 0

if flower == "Roses":
    price = 5
    if flower_count > 80:
        price *= 0.9
elif flower == "Dahlias":
    price = 3.8
    if flower_count > 90:
        price *= 0.85
elif flower == "Tulips":
    price = 2.8
    if flower_count > 80:
        price *= 0.85
elif flower == "Narcissus":
    price = 3
    if flower_count < 120:
        price *= 1.15
elif flower == "Gladiolus":
    price = 2.5
    if flower_count < 80:
        price *= 1.2


cost = flower_count * price
difference = abs(budget - cost)

if budget >= cost:
    print(f"Hey, you have a great garden with {flower_count} {flower} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
