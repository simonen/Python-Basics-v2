fuel = input()
fuel_volume = float(input())
discount_card = input()

price = 0
is_discount = False

if discount_card == "Yes":
    is_discount = True

if fuel == "Gasoline":
    price = 2.22
    if is_discount:
        price = 2.22 - 0.18
elif fuel == "Diesel":
    price = 2.33
    if is_discount:
        price = 2.33 - 0.12
elif fuel == "Gas":
    price = 0.93
    if is_discount:
        price = 0.93 - 0.08

if 20 < fuel_volume <= 25:
    price *= 0.92
elif fuel_volume > 25:
    price *= 0.9

cost = fuel_volume * price

print(f"{cost:.2f} lv.")
