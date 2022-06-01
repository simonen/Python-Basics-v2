import math

days = int(input())
food_provision = int(input())
dog_feed = float(input())
cat_feed = float(input())
turtle_feed = float(input())

food_needed = days * (dog_feed + cat_feed + turtle_feed / 1000)
difference = abs(food_needed - food_provision)

if food_needed <= food_provision:
    print(f"{math.floor(difference)} kilos of food left.")
else:
    print(f"{math.ceil(difference)} more kilos of food are needed.")