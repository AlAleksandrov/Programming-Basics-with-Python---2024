amount = float(input())

counter_coins = 0

while True:
    if amount == 0:
        break

    if amount >= 2:
        amount -= 2
    elif amount >= 1:
        amount -= 1
    elif amount >= 0.50:
        amount -= 0.50
    elif amount >= 0.20:
        amount -= 0.20
    elif amount >= 0.10:
        amount -= 0.10
    elif amount >= 0.05:
        amount -= 0.05
    elif amount >= 0.02:
        amount -= 0.02
    elif amount >= 0.01:
        amount -= 0.01

    counter_coins += 1
    amount = round(amount, 2)

print(f'{counter_coins}')