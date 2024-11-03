days_number = int(input())
room_type = input()
evaluation = input()

discount = 0
room_price = 0

if room_type == 'room for one person':
    discount = 0
    room_price = (days_number - 1) * 18.00 * (1 - discount)
elif room_type == 'apartment':
    if days_number < 10:
        discount = 0.30
        room_price = (days_number - 1) * 25.00 * (1 - discount)
    elif days_number <= 15:
        discount = 0.35
        room_price = (days_number - 1) * 25.00 * (1 - discount)
    else:
        discount = 0.50
        room_price = (days_number - 1) * 25.00 * (1 - discount)
elif room_type == 'president apartment':
    if days_number < 10:
        discount = 0.10
        room_price = (days_number - 1) * 35.00 * (1 - discount)
    elif days_number <= 15:
        discount = 0.15
        room_price = (days_number - 1) * 35.00 * (1 - discount)
    else:
        discount = 0.20
        room_price = (days_number - 1) * 35.00 * (1 - discount)

if evaluation == 'positive':
    room_price *= (1 + 0.25)
elif evaluation == 'negative':
    room_price *= (1 - 0.10)

print(f"{room_price :.2f}")
