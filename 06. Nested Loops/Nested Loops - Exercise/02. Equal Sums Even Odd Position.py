start_int = int(input())
end_int = int(input())

for n in range(start_int, end_int + 1):
    number_to_str = str(n)
    even_sum = 0
    odd_sum = 0
    for index, digit in enumerate(number_to_str):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if even_sum == odd_sum:
        print(n, end=' ')

