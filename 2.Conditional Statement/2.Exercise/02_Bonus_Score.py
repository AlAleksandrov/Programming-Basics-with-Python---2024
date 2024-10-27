number = int(input())

if number <= 100:
    bonus_point = 5
elif number <= 1000:
    bonus_point = number * 0.20
else:
    bonus_point = number * 0.10

additional_bonus_point =0
if number % 2 == 0:
    additional_bonus_point = 1

if number % 10 == 5:
    additional_bonus_point = 2

bonus = bonus_point + additional_bonus_point
total_bonus = number + bonus

print(bonus)
print(total_bonus)