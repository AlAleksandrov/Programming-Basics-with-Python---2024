number = int(input())
result = ''

for i in range(1111, 9999 + 1):
    number_as_string = str(i)
    is_special = True

    for n in number_as_string:
        digit = int(n)
        if digit == 0 or number % digit != 0:
            is_special = False
            break

    if is_special:
        print(f"{number_as_string}", end=' ')
