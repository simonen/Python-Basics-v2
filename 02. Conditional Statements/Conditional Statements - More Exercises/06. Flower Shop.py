import math

magnolia = int(input())
zumbuli = int(input())
roses = int(input())
cacti = int(input())
money_target = float(input())

profit = (magnolia * 3.25 + zumbuli * 4 + roses * 3.5 + cacti * 8) * 0.95
difference = abs(money_target - profit)

if profit >= money_target:
    print(f"She is left with {math.floor(difference)} leva.")
else:
    print(f"She will have to borrow {math.ceil(difference)} leva.")
