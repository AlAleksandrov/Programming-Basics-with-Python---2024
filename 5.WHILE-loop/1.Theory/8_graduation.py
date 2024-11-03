student = input()

grade = 1
score = total_score = 0.00
exam_torn = 0


while True:
    score = float(input())
    if score < 4:
        exam_torn += 1
        if exam_torn > 1:
            print(f'{student} has been excluded at {grade} grade')
            break
        continue

    total_score += score

    if grade == 12:
        average_score = total_score / grade
        print(f'{student} graduated. Average grade: {average_score:.2f}')
        break

    grade += 1
