veggie_price = float(input())
fruit_price = float(input())
veggie_kg = int(input())
fruit_kg = int(input())

profit = (veggie_kg * veggie_price + fruit_price * fruit_kg) / 1.94

print(f"{profit:.2f}")