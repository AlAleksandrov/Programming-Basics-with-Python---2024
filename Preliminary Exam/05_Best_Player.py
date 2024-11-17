import sys

command = input()
is_player = False
is_hat_trick = False
is_the_best = False
max_goals = -sys.maxsize
max_goals_player = ''

while True:
    if command == "END":
        break

    player_name = command
    command = input()
    number_goals = int(command)

    if 1 <= number_goals <= 2:
        is_player = True
        if max_goals < number_goals:
            max_goals = number_goals
            max_goals_player = player_name
    elif 3 <= number_goals <= 9:
        is_hat_trick = True
        if max_goals < number_goals:
            max_goals = number_goals
            max_goals_player = player_name
    elif number_goals >= 10:
        is_the_best = True
        if max_goals < number_goals:
            max_goals = number_goals
            max_goals_player = player_name
        break

    command = input()

if is_the_best or is_hat_trick:
    print(f'{max_goals_player} is the best player!')
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
elif is_player:
    print(f'{max_goals_player} is the best player!')
    print(f"He has scored {max_goals} goals.")
