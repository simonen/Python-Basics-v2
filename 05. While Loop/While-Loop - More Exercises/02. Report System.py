target_money = int(input())
money_in = input()

card_in = 0
cash_in = 0
count_cs = 0
count_cc = 0
count = 0
while money_in != "End":
    is_valid = False
    if count % 2 == 0:  # cash
        if int(money_in) <= 100:
            cash_in += int(money_in)
            count_cs += 1
            is_valid = True
    elif int(money_in) >= 10:  # card
        card_in += int(money_in)
        count_cc += 1
        is_valid = True
    if is_valid:
        target_money -= int(money_in)
        print("Product sold!")
    else:
        print("Error in transaction!")
    if cash_in == 0:
        average_cs = 0
    else:
        average_cs = cash_in / count_cs
    if card_in == 0:
        average_cc = 0
    else:
        average_cc = card_in / count_cc
    if target_money <= 0:
        print(f"Average CS: {average_cs:.2f}")
        print(f"Average CC: {average_cc:.2f}")
        break
    count += 1
    money_in = input()
else:
    print(f"Failed to collect required money for charity.")

