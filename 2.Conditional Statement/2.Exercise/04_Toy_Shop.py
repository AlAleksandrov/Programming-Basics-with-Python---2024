price_excursion = float(input())
puzzles_count = int(input())
speaking_dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

price_puzzles = puzzles_count * 2.60
price_speaking_dolls = speaking_dolls_count * 3
price_teddy_bears = teddy_bears_count * 4.10
price_minions = minions_count * 8.20
price_trucks = trucks_count * 2

toys_count = puzzles_count + speaking_dolls_count + teddy_bears_count + minions_count + trucks_count
price_toys = price_puzzles + price_speaking_dolls + price_teddy_bears + price_minions + price_trucks

discount = 0
if toys_count >= 50:
    discount = 0.25

total_price = price_toys * (1 - discount)
income = total_price * 0.9
if income >= price_excursion:
    money_left = income - price_excursion
    print(f'Yes! {money_left :.2f} lv left.')
else:
    money_needed = price_excursion - income
    print(f'Not enough money! {money_needed :.2f} lv needed.')
