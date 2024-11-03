budget = int(input())
season = input()  # "Spring", "Summer", "Autumn" or "Winter";
fishmen = int(input())

price_ship = 0
discount = 0.0
extra_discount = 0.0

if season == 'Spring':
    price_ship = 3000
    if fishmen <= 6:
        discount = 0.10
    elif fishmen <= 11:
        discount = 0.15
    elif fishmen >= 12:
        discount = 0.25

elif season == 'Summer' or season == 'Autumn':
    price_ship = 4200
    if fishmen <= 6:
        discount = 0.10
    elif fishmen <= 11:
        discount = 0.15
    elif fishmen >= 12:
        discount = 0.25

elif season == 'Winter':
    price_ship = 2600
    if fishmen <= 6:
        discount = 0.10
    elif fishmen <= 11:
        discount = 0.15
    elif fishmen >= 12:
        discount = 0.25

if fishmen % 2 == 0 and season != 'Autumn':
    extra_discount = 0.05

total_price = price_ship * (1-discount) * (1 - extra_discount)

if budget >= total_price:
    money_left = budget - total_price
    print(f"Yes! You have {money_left :.2f} leva left.")
else:
    money_needed = total_price - budget
    print(f"Not enough money! You need {money_needed :.2f} leva.")
