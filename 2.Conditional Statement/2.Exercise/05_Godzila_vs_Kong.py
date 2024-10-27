budget = float(input())
walk_on_count = int(input())
price_outfit = float(input())

decor = budget * 0.1
discount = 0.0
if walk_on_count > 150:
    discount = 0.1

total_price = decor + price_outfit * walk_on_count * (1-discount)

if total_price > budget:
    money_needed = total_price - budget
    print('Not enough money!')
    print(f'Wingard needs {money_needed :.2f} leva more.')
else:
    money_left = budget - total_price
    print('Action!')
    print(f'Wingard starts filming with {money_left :.2f} leva left.')