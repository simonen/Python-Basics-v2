pool_volume = int(input())  # m3
first_pipe = int(input())  # hour
second_pipe = int(input())  # hour
hours_off = float(input())

water_in = hours_off * (first_pipe + second_pipe)
p1_water = hours_off * first_pipe
p2_water = hours_off * second_pipe
overflow = abs(pool_volume - water_in)
p1_percent = p1_water / water_in * 100
p2_percent = p2_water / water_in * 100
percent_full = water_in / pool_volume * 100

if water_in > pool_volume:
    print(f"For {hours_off} hours the pool overflows with {overflow} liters.")
else:
    print(f"The pool is {percent_full:.2f}% full. Pipe 1: {p1_percent:.2f}%. Pipe 2: {p2_percent:.2f}%.")
