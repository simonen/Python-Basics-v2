money = float(input())
target_year = int(input())
age = 18
for year in range(1800, target_year + 1):
    if year % 2 == 0:
        money -= 12000
    else:
        money -= 12000 + 50 * age
    age += 1

difference = abs(money)
if money >= 0:
    print(f"Yes! He will live a carefree life and will have {difference:.2f} dollars left.")
else:
    print(f"He will need {difference:.2f} dollars to survive.")