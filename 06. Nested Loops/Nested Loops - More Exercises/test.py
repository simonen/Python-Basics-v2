import string

letter_start = input()
letter_end = input()
letter_excl = input()

count = 0
for letter_f in range(ord(letter_start), ord(letter_end) + 1):
    count_f = 0
    count_s = 0
    count_t = 0
    if chr(letter_f) == letter_excl:
        count_f = 0
        continue
    else:
        count_f = 1
    for letter_s in range(ord(letter_start), ord(letter_end) + 1):
        if chr(letter_s) == letter_excl:
            count_s = 0
            continue
        else:
            count_s = 1
        for letter_t in range(ord(letter_start), ord(letter_end) + 1):
            if chr(letter_t) == letter_excl:
                count_t = 0
                continue
            else:
                count_t = 1
                if count_f + count_s + count_t == 3:
                    count += 1
                    print(f"{chr(letter_f)}{chr(letter_s)}{chr(letter_t)}", end=" ")
                    count_t = 0
print(f"{count}")
