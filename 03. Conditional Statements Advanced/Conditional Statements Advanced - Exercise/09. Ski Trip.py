stay = int(input())
room_type = input()
rate = input()

price = 0

if room_type == "room for one person":
    price = 18
elif room_type == "apartment":
    price = 25
    if stay < 10:
        price *= 0.7
    elif stay < 15:
        price *= 0.65
    elif stay > 15:
        price *= 0.5
elif room_type == "president apartment":
    price = 35
    if stay < 10:
        price *= 0.9
    elif stay < 15:
        price *= 0.85
    elif stay > 15:
        price *= 0.8

cost = price * (stay - 1)

if rate == "positive":
    cost *= 1.25
elif rate == "negative":
    cost *= 0.9

print(f"{cost:.2f}")