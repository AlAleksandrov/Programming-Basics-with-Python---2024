new_input = input()

sum_numbers = 0

while new_input != 'NoMoreMoney':
    number_new_input = float(new_input)

    if number_new_input >= 0:
        sum_numbers += number_new_input
        print(f'Increase: {number_new_input:.2f}')
    else:
        print('Invalid operation!')
        break

    new_input = input()

print(f'Total: {sum_numbers:.2f}')
