import math

vineyard_area = int(input())
grapes_m2 = float(input())
wine_target = int(input())
workers = int(input())

grapes_area = vineyard_area * 0.4
grapes_yield = grapes_area * grapes_m2

wine_yield = grapes_yield / 2.5

difference = abs(wine_yield - wine_target)
wine_per_worker = difference / workers

if wine_yield >= wine_target:
    print(f"Good harvest this year! Total wine: {math.ceil(wine_yield):.0f} liters.")
    print(f"{difference:.0f} liters left -> {math.ceil(wine_per_worker):.0f} liters per person.")
else:
    print(f"It will be a tough winter! More {math.floor(difference):.0f} liters wine needed.")

