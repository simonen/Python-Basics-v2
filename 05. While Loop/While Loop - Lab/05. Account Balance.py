deposit = input()

balance = 0

while deposit != "NoMoreMoney":
    if float(deposit) <= 0:
        print(f"Invalid operation!")
        break
    balance += float(deposit)
    print(f"Increase: {float(deposit):.2f}")
    deposit = input()

print(f"Total: {balance:.2f}")