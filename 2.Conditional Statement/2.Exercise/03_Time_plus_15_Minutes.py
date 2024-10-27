hours = int(input())
minutes = int(input())
time_plus_15_minutes = minutes + 15

if time_plus_15_minutes >= 60:
    minutes = time_plus_15_minutes - 60
    hours += 1
else:
    minutes = time_plus_15_minutes

if hours >= 24:
    hours = 0

print(f'{hours}:{minutes :02d}')
