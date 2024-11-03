excursion_money = float(input())
available_cash = float(input())

counter_day_spend = counter_days = 0

while True:
    type_action = input()  # "spend", "save"
    amount = float(input())
    counter_days += 1

    if type_action == 'spend':
        counter_day_spend += 1
        if available_cash <= amount:
            available_cash = 0
        else:
            available_cash = available_cash - amount

    elif type_action == 'save':
        counter_day_spend = 0
        available_cash += amount

    if counter_day_spend == 5:
        break

    if available_cash >= excursion_money:
        break

if counter_day_spend == 5:
    print("You can't save the money.")
    print(f'{counter_days}')

if available_cash >= excursion_money:
    print(f'You saved the money for {counter_days} days.')
