budget = float(input())
season = input()

car_class = ''
car_cost = 0
car_type = 'Jeep'

if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        car_cost = budget * 0.35
    elif season == "Winter":
        car_cost = budget * 0.65
elif budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        car_cost = budget * 0.45
    elif season == "Winter":
        car_cost = budget * 0.80
elif budget > 500:
    car_class = "Luxury class"
    car_cost = budget * 0.9

print(car_class)
print(f"{car_type} - {car_cost:.2f}")