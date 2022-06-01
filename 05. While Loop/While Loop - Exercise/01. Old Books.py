searched_book = input()
search_count = 0
current_book = input()

while current_book != "No More Books":
    if searched_book == current_book:
        print(f"You checked {search_count} books and found it.")
        break
    current_book = input()
    search_count += 1
else:
    print(f"The book you search is not here!")
    print(f"You checked {search_count} books.")

