deposit = float(input())
term = int(input())
interest_rate = float(input())

profit = deposit + term * ((deposit * interest_rate / 100) / 12)

print(profit)
