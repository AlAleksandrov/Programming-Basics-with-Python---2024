command = input()

prime_numbers_sum = nonprime_numbers_sum = 0

while command != 'stop':
    number = int(command)
    is_prime = True
    if number < 0:
        print('Number is negative.')
        command = input()
        continue

    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        prime_numbers_sum += number
    else:
        nonprime_numbers_sum += number

    command = input()

print(f"Sum of all prime numbers is: {prime_numbers_sum}")
print(f"Sum of all non prime numbers is: {nonprime_numbers_sum}")
