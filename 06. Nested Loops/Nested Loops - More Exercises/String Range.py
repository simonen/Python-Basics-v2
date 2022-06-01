alpha = "Hello pederasi"
count = 0
word = ''
for letter in alpha:
    count += 1
    if count > 1:
        word += letter
    else:
        continue
    if count == 0:
        break

print(word, end="")