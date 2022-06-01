loads = int(input())
price = 0
bus_load = 0
truck_load = 0
train_load = 0
total_cost = 0
total_weight = 0

for load in range(loads):
    weight = int(input())
    if weight <= 3:
        price = 200 * weight
        bus_load += weight
    elif weight <= 11:
        price = 175 * weight
        truck_load += weight
    elif weight >= 12:
        price = 120 * weight
        train_load += weight
    total_cost += price
    total_weight += weight

average_price = total_cost / total_weight
bus_p = bus_load / total_weight * 100
truck_p = truck_load / total_weight * 100
train_p = train_load / total_weight * 100

print(f"{average_price:.2f}")
print(f"{bus_p:.2f}%")
print(f"{truck_p:.2f}%")
print(f"{train_p:.2f}%")