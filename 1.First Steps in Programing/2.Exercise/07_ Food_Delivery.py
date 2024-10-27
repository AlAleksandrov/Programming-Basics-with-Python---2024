menu_chicken = int(input())
menu_fish = int(input())
menu_vegetarian = int(input())

total_menu_chicken = menu_chicken * 10.35
total_menu_fish = menu_fish * 12.40
total_menu_vegetarian = menu_vegetarian * 8.15
total_dessert = (total_menu_chicken + total_menu_fish + total_menu_vegetarian) * 20 /100
total_delivery = 2.50
all_total = total_menu_chicken + total_menu_fish + total_menu_vegetarian + total_dessert + total_delivery

print(all_total)