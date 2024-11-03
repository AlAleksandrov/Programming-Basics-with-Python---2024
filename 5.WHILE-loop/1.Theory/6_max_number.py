import sys

new_input = input()

max_number = -sys.maxsize

while new_input != 'Stop':
    number_new_input = int(new_input)

    if max_number < number_new_input:
        max_number = number_new_input

    new_input = input()

print(f'{max_number}')
