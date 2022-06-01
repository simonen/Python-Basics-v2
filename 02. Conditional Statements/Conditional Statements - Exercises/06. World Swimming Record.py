record = float(input()) #seconds
distance = float(input()) #meters
speed = float(input()) #seconds to swim 1 meter

delay = 12.5 * (distance // 15) #seconds
ivan_time = distance * speed + delay

difference = abs(record - ivan_time)

if record > ivan_time:
    print(f"Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")


