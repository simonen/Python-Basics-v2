age = int(input())
wmachine_price = float(input())
toy_price = int(input())

toys_money = 0
money = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        money += 5 * i - 1
    else:
        toys_money += toy_price

total_money = money + toys_money
difference = abs(total_money - wmachine_price)

if total_money >= wmachine_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")