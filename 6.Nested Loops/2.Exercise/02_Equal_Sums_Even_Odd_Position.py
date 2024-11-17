num_1 = int(input())
num_2 = int(input())
number = 0

for number in range(num_1, num_2 + 1):
    sum_even = 0
    sum_odd = 0
    number_as_string = str(number)
    for idx, d in enumerate(number_as_string):

        digit = int(d)
        if idx % 2 == 0:
            sum_even += digit
        else:
            sum_odd += digit

    if sum_even == sum_odd:
        print(number_as_string, end=" ")
