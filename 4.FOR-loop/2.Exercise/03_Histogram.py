num = int(input())

count_p1 = count_p2 = count_p3 = count_p4 = count_p5 = 0

for num in range(1, num + 1):
    new_number = int(input())

    if new_number < 200:
        count_p1 += 1
    elif new_number <= 399:
        count_p2 += 1
    elif new_number <= 599:
        count_p3 += 1
    elif new_number <= 799:
        count_p4 += 1
    else:
        count_p5 += 1

percent1 = count_p1 / num * 100
percent2 = count_p2 / num * 100
percent3 = count_p3 / num * 100
percent4 = count_p4 / num * 100
percent5 = count_p5 / num * 100

print(f'{percent1 :.2f}%')
print(f'{percent2 :.2f}%')
print(f'{percent3 :.2f}%')
print(f'{percent4 :.2f}%')
print(f'{percent5 :.2f}%')
