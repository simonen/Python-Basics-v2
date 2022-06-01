projection = input()
rows = int(input())
cols = int(input())

price = 0

if projection == "Premiere":
    price = 12
elif projection == "Normal":
    price = 7.5
elif projection == "Discount":
    price = 5

income = rows * cols * price

print(f"{income:.2f} leva")

