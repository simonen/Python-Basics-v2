number = int(input())

for n in range(1111, 10000):
    divisions = 0
    n_to_string = str(n)
    for index, digit in enumerate(n_to_string):
        if int(digit) == 0:
            break
        if number % int(digit) == 0:
            divisions += 1
        if divisions == 4:
            print(n, end=" ")
