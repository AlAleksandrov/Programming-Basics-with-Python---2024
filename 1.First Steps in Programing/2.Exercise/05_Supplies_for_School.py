pens_packages = int(input())
markers_packages = int(input())
thinner_liters = int(input())
discount_percent = int(input())

# Да се отпечата на конзолата колко пари ще са нужни на Ани, за да си плати сметката.
total = pens_packages * 5.80 + markers_packages * 7.20 + thinner_liters * 1.20
total_with_discount = total * (1 - discount_percent / 100)

print(total_with_discount)

