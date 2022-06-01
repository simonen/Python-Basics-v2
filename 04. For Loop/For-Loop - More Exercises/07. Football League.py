s_capacity = int(input())
fans = int(input())

sector = ''
a_count = 0
b_count = 0
v_count = 0
g_count = 0

for fan in range(fans):
    sector = input()
    if sector == "A":
        a_count += 1
    elif sector == "B":
        b_count += 1
    elif sector == "V":
        v_count += 1
    elif sector == "G":
        g_count += 1

stad_capacity_p = fans / s_capacity * 100
a_percent = a_count / fans * 100
b_percent = b_count / fans * 100
v_percent = v_count / fans * 100
g_percent = g_count / fans * 100

print(f"{a_percent:.2f}%")
print(f"{b_percent:.2f}%")
print(f"{v_percent:.2f}%")
print(f"{g_percent:.2f}%")
print(f"{stad_capacity_p:.2f}%")