age = int(input())
washing_machine_price = float(input())
toys_price = int(input())

money = 0
toys = 0

for num in range(1, age + 1):

    if num % 2 == 0:
        money += num * 5
        money -= 1
    else:
        toys += 1

total_toys_price = toys * toys_price
total_amount = total_toys_price + money

if total_amount >= washing_machine_price:
    money_left = total_amount - washing_machine_price
    print(f'Yes! {money_left :.2f}')
else:
    money_needed = washing_machine_price - total_amount
    print(f'No! {money_needed :.2f}')
