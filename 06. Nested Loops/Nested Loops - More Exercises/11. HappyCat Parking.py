days = int(input())
hours = int(input())
total_bill = 0

for day in range(1, days + 1):
    daily_bill = 0
    price = 0
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            price += 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            price += 1.25
        else:
            price += 1
        daily_bill = price
    print(f"Day: {day} - {daily_bill:.2f} leva")
    total_bill += daily_bill

print(f"Total: {total_bill:.2f} leva")