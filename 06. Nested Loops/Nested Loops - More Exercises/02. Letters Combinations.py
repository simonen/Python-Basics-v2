import string

letter_start = input()
letter_end = input()
letter_excl = input()

count = 0
for letter_f in range(ord(letter_start), ord(letter_end) + 1):
    if chr(letter_f) == letter_excl:
        continue
    for letter_s in range(ord(letter_start), ord(letter_end) + 1):
        if chr(letter_s) == letter_excl:
            continue
        for letter_t in range(ord(letter_start), ord(letter_end) + 1):
            if chr(letter_t) == letter_excl:
                continue
            else:
                count += 1
                print(f"{chr(letter_f)}{chr(letter_s)}{chr(letter_t)}", end=" ")
print(f"{count}")
