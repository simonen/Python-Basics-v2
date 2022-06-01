import string
alpha = list(string.ascii_letters)
letter = input()
word = ""
valid_word = ""
n_count = 0
o_count = 0
c_count = 0

while letter != "End":
    if letter not in alpha:
        letter = ""
    if letter == "n" and n_count == 0:
        n_count = 1
        letter = ""
    elif letter == "o" and o_count == 0:
        o_count = 1
        letter = ""
    elif letter == "c" and c_count == 0:
        c_count = 1
        letter = ""
    if (c_count + n_count + o_count) == 3:
        n_count = 0
        o_count = 0
        c_count = 0
        word += " "
        valid_word = word
    word += letter
    letter = input()

print(valid_word)



