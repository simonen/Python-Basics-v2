destination = ''
money_target = 0

while destination != "End":
    destination = input()
    if destination == "End":
        break
    money_target = float(input())
    money_available = 0
    while money_target > money_available:
        saved_money = float(input())
        money_available += saved_money
    print(f"Going to {destination}!")

    