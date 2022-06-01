n = int(input())

even_sum = 0
odd_sum = 0
oddMin = 1000000
oddMax = -1000000
evenMin = 1000000
evenMax = -1000000

for i in range(1, n + 1):
    number = float(input())
    if i % 2 == 0:
        even_sum += number
        if number > evenMax:
            evenMax = number
        if number < evenMin:
            evenMin = number
    else:
        odd_sum += number
        if number > oddMax:
            oddMax = number
        if number < oddMin:
            oddMin = number

if oddMax == -1000000:
    oddMax = "No"
else:
    oddMax = f"{oddMax:.2f}"
if oddMin == 1000000:
    oddMin = "No"
else:
    oddMin = f"{oddMin:.2f}"
if evenMax == -1000000:
    evenMax = "No"
else:
    evenMax = f"{evenMax:.2f}"
if evenMin == 1000000:
    evenMin = "No"
else:
    evenMin = f"{evenMin:.2f}"

print(f"OddSum={odd_sum:.2f},")
print(f"OddMin=" + oddMin + ",")
print("OddMax=" + oddMax + ",")
print(f"EvenSum={even_sum:.2f},")
print(f"EvenMin=" + evenMin + ",")
print(f"EvenMax=" + evenMax)


