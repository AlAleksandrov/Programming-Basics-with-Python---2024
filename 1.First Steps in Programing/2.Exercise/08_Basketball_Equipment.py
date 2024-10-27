annual_fee = int(input())

sneakers = annual_fee * (1 - 40 / 100)
equip = sneakers * (1 - 20 / 100)
ball = equip / 4
accessories = ball / 5
total_expenses = annual_fee + sneakers + equip + ball + accessories

print(total_expenses)
