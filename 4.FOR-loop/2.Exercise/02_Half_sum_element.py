import sys

num = int(input())

max_number = -sys.maxsize
sum_numbers = 0

for _ in range(num):
    new_number = int(input())
    sum_numbers += new_number

    if new_number >= max_number:
        max_number = new_number

if max_number == sum_numbers / 2:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    diff = abs(max_number - (sum_numbers - max_number))
    print('No')
    print(f'Diff = {diff}')
