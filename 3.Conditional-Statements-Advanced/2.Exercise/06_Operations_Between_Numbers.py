N1 = int(input())
N2 = int(input())
operator_type = input()

result = 0
even_odd = ''
text_print = ''

if operator_type == '+':
    result = N1 + N2
    if result % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
    text_print = f"{N1} {operator_type} {N2} = {result} - {even_odd}"

elif operator_type == '-':
    result = N1 - N2
    if result % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
    text_print = f"{N1} {operator_type} {N2} = {result} - {even_odd}"

elif operator_type == '*':
    result = N1 * N2
    if result % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
    text_print = f"{N1} {operator_type} {N2} = {result} - {even_odd}"

elif operator_type == '/':
    if N2 == 0:
        text_print = f"Cannot divide {N1} by zero"
    else:
        result = N1 / N2
        text_print = f"{N1} / {N2} = {result :.2f}"

elif operator_type == '%':
    if N2 == 0:
        text_print = f"Cannot divide {N1} by zero"
    else:
        result = N1 % N2
        text_print = f"{N1} % {N2} = {result}"

print(text_print)
