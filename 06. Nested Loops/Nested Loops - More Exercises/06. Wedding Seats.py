last_sector = input()
rows_A = int(input())
odd_row_seats = int(input())

count = 0
rows = rows_A

for sector in range(65, ord(last_sector) + 1):
    for row in range(1, rows + 1):
        if row % 2 == 0:
            seats = 99 + odd_row_seats
        else:
            seats = 97 + odd_row_seats
        for seat in range(97, seats):
            print(chr(sector) + str(row) + chr(seat))
            count += 1
    rows += 1

print(count)

