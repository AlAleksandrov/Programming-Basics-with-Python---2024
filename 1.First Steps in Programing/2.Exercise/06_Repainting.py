nilon = int(input())
paint = int(input())
thinner = int(input())
work_hours = int(input())

total_for_nilon = (nilon + 2) * 1.50
total_for_paint = (paint * 1.1) * 14.50
total_for_thinner = thinner * 5.00
total_for_bags = 0.40
total_for_materials = total_for_nilon + total_for_paint + total_for_thinner + total_for_bags
total_for_work_hours = (total_for_materials * 0.3) * work_hours
all_totals = total_for_materials + total_for_work_hours

print(all_totals)
