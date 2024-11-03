number_unsatisfactory_ratings = int(input())

total_score = average_score = problem_counter = counter = 0
is_enough = False
is_unsatisfactory = False
task = ''

while True:
    command = input()

    if command == 'Enough':
        is_enough = True
        break

    task = command
    score = int(input())
    counter += 1
    total_score += score
    average_score = total_score / counter

    if score <= 4:
        problem_counter += 1
        if problem_counter == number_unsatisfactory_ratings:
            is_unsatisfactory = True
            break

if is_enough:
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {counter}')
    print(f'Last problem: {task}')

if is_unsatisfactory:
    print(f'You need a break, {number_unsatisfactory_ratings} poor grades.')
