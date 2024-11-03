num = int(input())

left_sum = 0
right_sum = 0

for i in range(2 * num):
    new_number = int(input())

    if i <= num - 1:
        left_sum += new_number
    else:
        right_sum += new_number

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    diff = abs(left_sum - right_sum)
    print(f'No, diff = {diff}')
