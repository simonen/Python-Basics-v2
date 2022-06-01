travel = float(input())
puzzle = int(input())
doll = int(input())
teddy_bear = int(input())
mignon = int(input())
truck = int(input())

income = (puzzle * 2.6 + doll * 3 + teddy_bear * 4.1 + mignon * 8.2 + truck * 2) * 0.9

toys_sold = puzzle + doll + teddy_bear + mignon + truck

if toys_sold >= 50:
    income *= 0.75
difference = abs(travel - income)
if income >= travel:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")
