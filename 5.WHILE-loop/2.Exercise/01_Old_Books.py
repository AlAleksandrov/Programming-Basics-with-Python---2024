favourite_book = input()
searching = input()

counter = 0

while searching != "No More Books":
    book = searching
    if book == favourite_book:
        break

    counter += 1

    searching = input()

if searching == "No More Books":
    print('The book you search is not here!')
    print(f'You checked {counter} books.')
else:
    print(f'You checked {counter} books and found it.')
