length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = (length * width * height) / 1000 #dm3
reserved_volume = volume * percent / 100
water_volume = volume - reserved_volume

print(water_volume)


