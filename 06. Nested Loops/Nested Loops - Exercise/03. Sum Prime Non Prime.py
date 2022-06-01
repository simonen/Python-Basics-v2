primes = 0
non_primes = 0
number = 0

while str(number) != "stop":
    for k in range(2, int(number)):
        if int(number) % k == 0:
            non_primes += int(number)
            break
    else:
        primes += int(number)
    number = input()
    if number == "stop":
        break
    if int(number) < 0:
        print(f"Number is negative.")
        number = 0

print(f"Sum of all prime numbers is: {primes}")
print(f"Sum of all non prime numbers is: {non_primes}")
