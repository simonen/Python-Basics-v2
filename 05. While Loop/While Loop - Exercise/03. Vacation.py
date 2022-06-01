money_target = float(input())
money_available = float(input())

days = 0
spending_spree = 0

while money_target > money_available:
    action = input()
    amount = float(input())
    if action == "spend":
        spending_spree += 1
        if amount >= money_available:
            money_available = 0
        else:
            money_available -= amount
    elif action == "save":
        money_available += amount
        spending_spree = 0
    days += 1
    if spending_spree == 5:
        print("You can't save the money.")
        print(days)
        break
else:
    print(f"You saved the money for {days} days.")
