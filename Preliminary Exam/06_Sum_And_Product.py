n = int(input())
sum_abcd = 0
product_abcd = 0
is_found = False
number = ''

for a in range(1, 9 + 1):
    if is_found:
        break
    if a == 9 or a == 10:
        for b in range(9, a + 1):
            if is_found:
                break
            for c in range(0, 9 + 1):
                if is_found:
                    break
                if c == 9 or c == 10:
                    for d in range(9, c + 1):
                        sum_abcd = a + b + c + d
                        product_abcd = a * b * c * d
                        if sum_abcd == product_abcd and n % 10 == 5:
                            is_found = True
                            number = f"{a}{b}{c}{d}"
                            break
                        elif product_abcd // sum_abcd == 3 and n % 3 == 0:
                            is_found = True
                            number = f"{d}{c}{b}{a}"
                            break
                else:
                    for d in range(9, c, -1):
                        sum_abcd = a + b + c + d
                        product_abcd = a * b * c * d
                        if sum_abcd == product_abcd and n % 10 == 5:
                            is_found = True
                            number = f"{a}{b}{c}{d}"
                            break
                        elif product_abcd // sum_abcd == 3 and n % 3 == 0:
                            is_found = True
                            number = f"{d}{c}{b}{a}"
                            break
    else:
        for b in range(9, a, -1):
            if is_found:
                break
            for c in range(0, 9 + 1):
                if is_found:
                    break
                if c == 9 or c == 10:
                    for d in range(9, c + 1):
                        sum_abcd = a + b + c + d
                        product_abcd = a * b * c * d
                        if sum_abcd == product_abcd and n % 10 == 5:
                            is_found = True
                            number = f"{a}{b}{c}{d}"
                            break
                        elif product_abcd // sum_abcd == 3 and n % 3 == 0:
                            is_found = True
                            number = f"{d}{c}{b}{a}"
                            break
                else:
                    for d in range(9, c, -1):
                        sum_abcd = a + b + c + d
                        product_abcd = a * b * c * d
                        if sum_abcd == product_abcd and n % 10 == 5:
                            is_found = True
                            number = f"{a}{b}{c}{d}"
                            break
                        elif product_abcd // sum_abcd == 3 and n % 3 == 0:
                            is_found = True
                            number = f"{d}{c}{b}{a}"
                            break

if is_found:
    print(f'{number}')
else:
    print('Nothing found')
