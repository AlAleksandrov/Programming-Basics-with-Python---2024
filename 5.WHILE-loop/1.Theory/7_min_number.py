import sys

new_input = input()

min_number = sys.maxsize

while new_input != 'Stop':
    number_new_input = int(new_input)

    if min_number > number_new_input:
        min_number = number_new_input

    new_input = input()

print(f'{min_number}')
