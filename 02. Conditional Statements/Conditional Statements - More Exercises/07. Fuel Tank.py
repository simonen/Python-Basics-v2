fuel = input()
tank_fuel = float(input())

fuel_type = ''
is_valid = True

if fuel == "Diesel":
    fuel_type = "diesel"
elif fuel == "Gasoline":
    fuel_type = "gasoline"
elif fuel == "Gas":
    fuel_type = "gas"
else:
    print(f"Invalid fuel!")
    is_valid = False

if is_valid:
    if tank_fuel >= 25:
        print(f"You have enough {fuel_type}.")
    else:
        print(f"Fill your tank with {fuel_type}!")

