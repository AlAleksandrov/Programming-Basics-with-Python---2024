groups_of_climbers = int(input())

climbers_musala = 0
climbers_monblan = 0
climbers_kilimanjaro = 0
climbers_k2 = 0
climbers_everest = 0

for _ in range(groups_of_climbers):
    number_people_in_group = int(input())

    if number_people_in_group <= 5:
        climbers_musala += number_people_in_group
    elif number_people_in_group <= 12:
        climbers_monblan += number_people_in_group
    elif number_people_in_group <= 25:
        climbers_kilimanjaro += number_people_in_group
    elif number_people_in_group <= 40:
        climbers_k2 += number_people_in_group
    else:
        climbers_everest += number_people_in_group

all_peoples = climbers_musala + climbers_monblan + climbers_kilimanjaro + climbers_k2 + climbers_everest
percent_climbers_musala = climbers_musala / all_peoples * 100
percent_climbers_monblan = climbers_monblan / all_peoples * 100
percent_climbers_kilimanjaro = climbers_kilimanjaro / all_peoples * 100
percent_climbers_k2 = climbers_k2 / all_peoples * 100
percent_climbers_everest = climbers_everest / all_peoples * 100

print(f'{percent_climbers_musala :.2f}%')
print(f'{percent_climbers_monblan :.2f}%')
print(f'{percent_climbers_kilimanjaro :.2f}%')
print(f'{percent_climbers_k2 :.2f}%')
print(f'{percent_climbers_everest :.2f}%')
