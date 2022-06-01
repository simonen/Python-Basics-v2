months = int(input())

electricity = 0
water = 0
internet = 0
others = 0

for month in range(months):
    e_bill = float(input())
    water += 20
    internet += 15
    others += (e_bill + 20 + 15) * 1.2
    electricity += e_bill

average = (electricity + water + internet + others) / months
print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {others:.2f} lv")
print(f"Average: {average:.2f} lv")