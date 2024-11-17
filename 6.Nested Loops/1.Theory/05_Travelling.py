while True:
    destination = input()
    if destination == 'End':
        break
    budget = float(input())
    money = 0.0

    while money < budget:
        some_money = float(input())
        money += some_money

    print(f'Going to {destination}!')
