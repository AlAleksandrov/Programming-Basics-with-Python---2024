day_of_the_week = input()
result = 0

if day_of_the_week == 'Monday' or day_of_the_week == "Tuesday" or day_of_the_week == 'Friday':
    result = 12
elif day_of_the_week == 'Wednesday' or day_of_the_week == 'Thursday':
    result = 14
elif day_of_the_week == 'Saturday' or day_of_the_week == 'Sunday':
    result = 16

print(result)
