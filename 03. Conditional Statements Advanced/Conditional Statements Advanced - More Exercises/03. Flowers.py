hrizantemi = int(input())
rozi = int(input())
laleta = int(input())
season = input()
holiday = input()

roses_count = rozi
laleta_count = laleta
flowers_count = hrizantemi + rozi + laleta

if season == "Spring" or season == "Summer":
    hrizantemi *= 2
    rozi *= 4.1
    laleta *= 2.5
elif season == "Autumn" or season == "Winter":
    hrizantemi *= 3.75
    rozi *= 4.5
    laleta *= 4.15

flowers_cost = hrizantemi + rozi + laleta

if season == "Spring" and laleta_count > 7:
    flowers_cost *= 0.95
if season == "Winter" and roses_count >= 10:
    flowers_cost *= 0.9
if holiday == "Y":
    flowers_cost *= 1.15
if flowers_count > 20:
    flowers_cost *= 0.8

bouquet_cost = flowers_cost + 2

print(f"{bouquet_cost:.2f}")
