control_value = int(input())

count = 0
password = ''
for a in range(1, 10):
    for b in range(1, 10):
        if a < b:
            for c in range(1, 10):
                for d in range(1, 10):
                    if (c > d) and (a * b + c * d) == control_value:
                        count += 1
                        print(f"{a}{b}{c}{d}", end=" ")
                        if count == 4:
                            password = f"{a}{b}{c}{d}"
print()
if count < 4:
    print("No!")
else:
    print(f"Password: {password}")
