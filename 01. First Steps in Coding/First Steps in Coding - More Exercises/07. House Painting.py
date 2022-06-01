#green_paint_cover = 3.4  # m2 per liter
#red_paint_cover = 4.3  # m2 per liter

# walls dimensions
house_height = float(input())
wall_length = float(input())
roof_height = float(input())

# Walls area
area_front_walls = house_height ** 2
area_side_walls = house_height * wall_length - 1.5 ** 2
house_area = 2 * (area_side_walls + area_front_walls - 1.2)

# Roof area
roof_area = 2 * house_height * wall_length + house_height * roof_height

green_paint_liters = house_area / 3.4
red_paint_liters = roof_area / 4.3

print(f"{green_paint_liters:.2f}")
print(f"{red_paint_liters:.2f}")
