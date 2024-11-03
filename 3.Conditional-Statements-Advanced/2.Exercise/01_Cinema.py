cinema_type = input()
r = int(input())
c = int(input())

tickets = r * c
price_ticket = 0.0

if cinema_type == 'Premiere':
    price_ticket = 12.00
elif cinema_type == 'Normal':
    price_ticket = 7.50
elif cinema_type == 'Discount':
    price_ticket = 5.00

total_price = tickets * price_ticket

print(f'{total_price :.2f} leva')