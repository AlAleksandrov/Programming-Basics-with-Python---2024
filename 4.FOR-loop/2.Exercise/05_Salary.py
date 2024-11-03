open_tabs = int(input())
salary = int(input())

for _ in range(open_tabs):
    website = input()

    if website == 'Facebook':
        salary -= 150
        if salary <= 0:
            break
    elif website == 'Instagram':
        salary -= 100
        if salary <= 0:
            break
    elif website == 'Reddit':
        salary -= 50
        if salary <= 0:
            break

if salary <= 0:
    print('You have lost your salary.')
else:
    print(salary)
