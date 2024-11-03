number = int(input())

sum_numbers = 0

while True:
    new_number = int(input())
    sum_numbers += new_number
    if sum_numbers >= number:
        break

print(f'{sum_numbers}')
