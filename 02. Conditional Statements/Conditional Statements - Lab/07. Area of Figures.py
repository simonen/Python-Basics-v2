import math

figure = input()

if figure == "square":
    square_side = float(input())
    square_area = square_side ** 2
    print(f"{square_area:.3f}")
elif figure == "rectangle":
    rect_side_a = float(input())
    rect_side_b = float(input())
    rect_area = rect_side_b * rect_side_a
    print(f"{rect_area:.3f}")
elif figure == "circle":
    radius = float(input())
    circle_area = radius ** 2 * math.pi
    print(f"{circle_area:.3f}")
elif figure == "triangle":
    triangle_side = float(input())
    triangle_height = float(input())
    triangle_area = triangle_side * triangle_height / 2
    print(f"{triangle_area:.3f}")