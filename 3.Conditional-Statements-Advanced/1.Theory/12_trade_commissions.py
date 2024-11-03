city = input()
sales_volume = float(input())
is_error = False
commission = 0.0

if city == "Sofia":
    if 0 <= sales_volume <= 500:
        commission = 0.05
    elif 500 <= sales_volume <= 1000:
        commission = 0.07
    elif 1000 <= sales_volume <= 10000:
        commission = 0.08
    elif 10000 <= sales_volume:
        commission = 0.12
    else:
        is_error = True
elif city == "Varna":
    if 0 <= sales_volume <= 500:
        commission = 0.045
    elif 500 <= sales_volume <= 1000:
        commission = 0.075
    elif 1000 <= sales_volume <= 10000:
        commission = 0.10
    elif 10000 <= sales_volume:
        commission = 0.13
    else:
        is_error = True
elif city == "Plovdiv":
    if 0 <= sales_volume <= 500:
        commission = 0.055
    elif 500 <= sales_volume <= 1000:
        commission = 0.08
    elif 1000 <= sales_volume <= 10000:
        commission = 0.12
    elif 10000 <= sales_volume:
        commission = 0.145
    else:
        is_error = True
else:
    is_error = True

total_price = sales_volume * commission

if is_error:
    print("error")
else:
    print(f'{total_price :.2f}')