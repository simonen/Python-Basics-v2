groups = int(input())

musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0
total_climbers = 0

for i in range(1, groups + 1):
    climbers = int(input())
    if climbers <= 5:
        musala += climbers
    elif climbers <= 12:
        monblan += climbers
    elif climbers <= 25:
        kilimandjaro += climbers
    elif climbers <= 40:
        k2 += climbers
    elif climbers >= 41:
        everest += climbers
    total_climbers += climbers

musala_p = musala / total_climbers * 100
monblan_p = monblan / total_climbers * 100
kilimandjaro_p = kilimandjaro / total_climbers * 100
k2_p = k2 / total_climbers * 100
everest_p = everest / total_climbers * 100

print(f"{musala_p:.2f}%")
print(f"{monblan_p:.2f}%")
print(f"{kilimandjaro_p:.2f}%")
print(f"{k2_p:.2f}%")
print(f"{everest_p:.2f}%")

