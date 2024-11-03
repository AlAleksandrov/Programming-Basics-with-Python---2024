month = input()  # May, June, July, August, September or October
nights_count = int(input())

price_studio = 0.0
price_apartment = 0.0
discount_studio = 0.0
discount_apartment = 0.0

if month == 'May' or month == 'October':
    price_studio = 50.00
    price_apartment = 65.00
    if 7 < nights_count <= 14:
        discount_studio = 0.05
    elif nights_count > 14:
        discount_studio = 0.30
        discount_apartment = 0.10
elif month == 'June' or month == 'September':
    price_studio = 75.20
    price_apartment = 68.70
    if nights_count > 14:
        discount_studio = 0.20
        discount_apartment = 0.10
elif month == 'July' or month == 'August':
    price_studio = 76.00
    price_apartment = 77.00
    if nights_count > 14:
        discount_apartment = 0.10

total_price_studio = nights_count * price_studio * (1 - discount_studio)
total_price_apartment = nights_count * price_apartment * (1 - discount_apartment)

print(f"Apartment: {total_price_apartment :.2f} lv.")
print(f"Studio: {total_price_studio :.2f} lv.")
