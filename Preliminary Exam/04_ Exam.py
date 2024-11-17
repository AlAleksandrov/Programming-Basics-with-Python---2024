number_students = int(input())
percentage_5_above = 0.0
percentage_4_above = 0.0
percentage_3_above = 0.0
percentage_2_above = 0.0
average_grade = 0.0
count1 = count2 = count3 = count4 =0

for num in range (1, number_students + 1):
    exam_grade = float(input())
    average_grade += exam_grade

    if 2.00 <= exam_grade <= 2.99:
        count1 += 1
    elif exam_grade <= 3.99:
        count2 += 1
    elif exam_grade <= 4.99:
        count3 += 1
    elif exam_grade >= 5.00:
        count4 += 1

percentage_2_above += count1 / number_students * 100
percentage_3_above += count2 / number_students * 100
percentage_4_above += count3 / number_students * 100
percentage_5_above += count4 / number_students * 100
average_grade = average_grade / number_students

print(f"Top students: {percentage_5_above:.2f}%")
print(f"Between 4.00 and 4.99: {percentage_4_above:.2f}%")
print(f"Between 3.00 and 3.99: {percentage_3_above:.2f}%")
print(f"Fail: {percentage_2_above:.2f}%")
print(f"Average: {average_grade:.2f}")
