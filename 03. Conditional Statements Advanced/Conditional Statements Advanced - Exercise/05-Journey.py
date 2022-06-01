budget = float(input())
season = input()

destination = ''
accommodation = ''
money_spent = 0

if season == "summer":
    accommodation = "Camp"
elif season == "winter":
    accommodation = "Hotel"

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        money_spent = 0.3 * budget
    elif season == "winter":
        money_spent = 0.7 * budget
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        money_spent = 0.4 * budget
    elif season == "winter":
        money_spent = 0.8 * budget
else:
    destination = "Europe"
    money_spent = 0.9 * budget
    accommodation = "Hotel"

print(f"Somewhere in {destination}")
print(f"{accommodation} - {money_spent:.2f}")
