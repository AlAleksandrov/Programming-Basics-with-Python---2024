dancers_number = int(input())
points_number = float(input())
season = input()
place = input()
discount = 0
donation = 0.75

cash_price = 0.0

if season == 'summer':
    if place == 'Bulgaria':
        discount = 0.05
        cash_price = points_number * dancers_number
        cash_price = cash_price * (1 - discount)
    elif place == 'Abroad':
        discount = 0.10
        cash_price = points_number * dancers_number * 1.5
        cash_price = cash_price * (1 - discount)
elif season == 'winter':
    if place == 'Bulgaria':
        discount = 0.08
        cash_price = points_number * dancers_number
        cash_price = cash_price * (1 - discount)
    elif place == 'Abroad':
        discount = 0.15
        cash_price = points_number * dancers_number * 1.5
        cash_price = cash_price * (1 - discount)

total_cash = cash_price * (1 - donation) / dancers_number
donation_cash = cash_price * donation

print(f'Charity - {donation_cash:.2f}')
print(f'Money per dancer - {total_cash:.2f}')
