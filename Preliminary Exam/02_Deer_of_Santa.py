import math
days_missing = int(input())
kg_foods = int(input())
kg_food_first_deer_per_day = float(input())
kg_food_second_deer_per_day = float(input())
kg_food_third_deer_per_day = float(input())

needed_food_first_deer = days_missing * kg_food_first_deer_per_day
needed_food_second_deer = days_missing * kg_food_second_deer_per_day
needed_food_third_deer = days_missing * kg_food_third_deer_per_day

total_needed_food = needed_food_first_deer + needed_food_second_deer + needed_food_third_deer

if kg_foods >= total_needed_food:
    kg_left = math.floor(kg_foods - total_needed_food)
    print(f'{kg_left} kilos of food left.')
else:
    kg_needed = math.ceil(total_needed_food - kg_foods)
    print(f'{kg_needed} more kilos of food are needed.')
