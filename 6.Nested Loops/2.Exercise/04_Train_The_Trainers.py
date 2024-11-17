number_peoples_jury = int(input())
command = input()
count_presentation = total_avg_evaluation = 0
evaluation = 0

while command != 'Finish':
    presentation = command
    count_presentation += 1
    avg_evaluation = 0.0
    all_evaluations = 0.0
    for _ in range(number_peoples_jury):
        evaluation = float(input())
        all_evaluations += evaluation

    avg_evaluation = all_evaluations / number_peoples_jury
    print(f'{presentation} - {avg_evaluation :.2f}.')
    total_avg_evaluation += avg_evaluation

    command = input()

print(f'Student\'s final assessment is {(total_avg_evaluation / count_presentation) :.2f}.')
