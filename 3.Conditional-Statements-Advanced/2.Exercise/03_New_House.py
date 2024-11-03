flowers_type = input()  # "Roses", "Dahlias", "Tulips", "Narcissus" or "Gladiolus"
flowers_count = int(input())
budget = int(input())

flowers_price = 0.0
discount =0.0

if flowers_type == 'Roses':
    if flowers_count > 80:
        discount = 0.10
    flowers_price = 5.00
elif flowers_type == 'Dahlias':
    if flowers_count > 90:
        discount = 0.15
    flowers_price = 3.80
elif flowers_type == 'Tulips':
    if flowers_count > 80:
        discount = 0.15
    flowers_price = 2.80
elif flowers_type == 'Narcissus':
    if flowers_count < 120:
        discount = - 0.15
    flowers_price = 3.00
elif flowers_type == 'Gladiolus':
    if flowers_count < 80:
        discount = - 0.20
    flowers_price = 2.50

total_price = flowers_count * flowers_price * (1-discount)

if budget >= total_price:
    money_left = budget - total_price
    print(f"Hey, you have a great garden with {flowers_count} {flowers_type} and {money_left :.2f} leva left.")
else:
    money_needed = total_price - budget
    print(f"Not enough money, you need {money_needed :.2f} leva more.")
