command = input()

count_standard = count_student = count_kid = 0
percentage_full_hall = 0

while command != 'Finish':
    movie = command
    free_seats = int(input())
    total_seats = free_seats
    type_tickets = input()
    while type_tickets != 'End':

        if type_tickets == 'standard':
            count_standard += 1
        elif type_tickets == 'student':
            count_student += 1
        elif type_tickets == 'kid':
            count_kid += 1

        free_seats -= 1
        if free_seats <= 0:
            break

        type_tickets = input()

    bought_tickets = total_seats - free_seats
    percentage_full_hall = bought_tickets / total_seats * 100
    print(f'{movie} - {percentage_full_hall :.2f}% full.')

    command = input()

total_tickets = count_standard + count_student + count_kid
percentage_student_tickets = count_student / total_tickets * 100
percentage_standard_tickets = count_standard / total_tickets * 100
percentage_kid_tickets = count_kid / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{percentage_student_tickets :.2f}% student tickets.")
print(f"{percentage_standard_tickets :.2f}% standard tickets.")
print(f"{percentage_kid_tickets :.2f}% kids tickets.")
