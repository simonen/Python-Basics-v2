width = int(input())
length = int(input())
height = int(input())

volume = width * length * height

while volume > 0:
    boxes = input()
    if boxes == "Done":
        break
    volume -= int(boxes)

if volume >= 0:
    print(f"{volume} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(volume)} Cubic meters more.")
