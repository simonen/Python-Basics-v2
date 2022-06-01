distance = int(input())
time_of_day = input()
transport = ''

taxi_rate = 0.9
bus_rate = 0.09
train_rate = 0.06

if time_of_day == "day":
    taxi_rate = 0.79

taxi_cost = 0.7 + taxi_rate * distance
bus_cost = bus_rate * distance
train_cost = train_rate * distance

if distance >= 100:
    transport = "train"
    print(f"{train_cost:.2f}")
elif distance >= 20:
    transport = "bus"
    print(f"{bus_cost:.2f}")
else:
    transport = "taxi"
    print(f"{taxi_cost:.2f}")
