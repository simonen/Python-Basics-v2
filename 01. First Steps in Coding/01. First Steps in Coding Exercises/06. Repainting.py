wrap = int(input())
paint = int(input())
diluent = int(input())
hours = int(input())

materials = wrap * 1.5 + 3 + paint * 14.5 * 1.1 + diluent * 5 + 0.4
labor_rate = materials * 0.3

total_cost = materials + hours * labor_rate

print(total_cost)