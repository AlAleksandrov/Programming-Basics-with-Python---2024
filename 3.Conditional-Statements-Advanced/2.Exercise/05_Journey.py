budget = float(input())
seasons = input()  # "summer” or "winter”

destination = ''
price = 0.0
vacation_type = ''

if budget <= 100:
    if seasons == 'summer':
        price = budget * 0.30
        destination = "Bulgaria"
        vacation_type = 'Camp'
    elif seasons == 'winter':
        price = budget * 0.70
        destination = "Bulgaria"
        vacation_type = 'Hotel'
elif budget <= 1000:
    if seasons == 'summer':
        price = budget * 0.40
        destination = "Balkans"
        vacation_type = 'Camp'
    elif seasons == 'winter':
        price = budget * 0.80
        destination = "Balkans"
        vacation_type = 'Hotel'
elif budget > 1000:
    price = budget * 0.90
    destination = "Europe"
    vacation_type = 'Hotel'

print(f"Somewhere in {destination}")
print(f"{vacation_type} - {price :.2f}")
