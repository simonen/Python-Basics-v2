width = float(input())
height = float(input())

columns = (height - 1) // 0.7
rows = width // 1.2
workplaces = rows * columns - 3

#print(columns)
#print(rows)
print(f"{workplaces:.0f}")