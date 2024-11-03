number = int(input())

next_number = 1

while True:
    if number < next_number:
        break
    print(f'{next_number}')
    next_number = (next_number * 2) + 1
