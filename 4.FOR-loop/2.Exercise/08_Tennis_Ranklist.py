tournaments = int(input())
starting_points = int(input())

points = 0
count = 0

for _ in range(tournaments):
    position = input()

    if position == 'W':
        points += 2000
        count += 1
    elif position == 'F':
        points += 1200
    elif position == 'SF':
        points += 720

total_points = starting_points + points
average_points = int(points / tournaments)
percent_win_tournaments = (count / tournaments) * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{percent_win_tournaments :.2f}%")
