name_artist = input()
academy_points = float(input())
assessors_number = int(input())

for _ in range(assessors_number):
    name_assessor = input()
    points_assessor = float(input())
    total_points_assessor = ((len(name_assessor) * points_assessor) / 2)
    academy_points += total_points_assessor
    if academy_points > 1250.5:
        break

if academy_points >= 1250.5:
    print(f'Congratulations, {name_artist} got a nominee for leading role with {academy_points :.1f}!')
else:
    points_needed = 1250.5 - academy_points
    print(f'Sorry, {name_artist} you need {points_needed :.1f} more!')
