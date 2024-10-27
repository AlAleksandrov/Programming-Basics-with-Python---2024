seconds_1 = int(input())
seconds_2 = int(input())
seconds_3 = int(input())

sum_seconds = seconds_1 + seconds_2 + seconds_3
minutes = sum_seconds // 60
seconds = sum_seconds % 60

print(f'{minutes}:{seconds:02d}')
