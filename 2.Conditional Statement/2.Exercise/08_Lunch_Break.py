from math import ceil
serial_name = input()
episode = int(input())
duration_of_the_pause = int(input())

lunch_time = 1/8 * duration_of_the_pause
rest_time = 1/4 * duration_of_the_pause

movie_time = (duration_of_the_pause - lunch_time - rest_time)
i_have_enough_time = abs(movie_time - episode)

if movie_time > episode:
    print(f'You have enough time to watch {serial_name} and left with {ceil(i_have_enough_time)} minutes free time.')
else:
    print(f"You don't have enough time to watch {serial_name}, you need {ceil(i_have_enough_time)} more minutes.")
