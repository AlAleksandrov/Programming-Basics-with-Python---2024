num = int(input())

odd_sum = 0
even_sum = 0

for idx in range(num):
    new_number = int(input())

    if idx % 2 == 0:
        even_sum += new_number
    else:
        odd_sum += new_number

if even_sum == odd_sum:
    print('Yes')
    print(f'Sum = {even_sum}')
else:
    diff = abs(even_sum - odd_sum)
    print("No")
    print(f'Diff = {diff}')
