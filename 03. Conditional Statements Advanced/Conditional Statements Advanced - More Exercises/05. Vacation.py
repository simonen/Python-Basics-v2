budget = float(input())
season = input()

location = 'Morocco'
accommodation = ''

if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        location = "Alaska"
        budget *= 0.65
    else:
        budget *= 0.45
elif budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        location = "Alaska"
        budget *= 0.8
    else:
        budget *= 0.6
elif budget > 3000:
    if season == "Summer":
        location = "Alaska"
    accommodation = "Hotel"
    budget *= 0.9

print(f"{location} - {accommodation} - {budget:.2f}")