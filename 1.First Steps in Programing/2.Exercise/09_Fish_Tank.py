length = int(input())  # cm3
width = int(input())  # cm3
high = int(input())  # cm3
percent_not_water = float(input())

capacity_in_cm = length * width * high
capacity_in_dm = capacity_in_cm / 1000
water_capacity = capacity_in_dm * (1 - percent_not_water / 100)

print(water_capacity)