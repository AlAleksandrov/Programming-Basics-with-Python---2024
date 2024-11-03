exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

time_exam_in_minutes = exam_hour * 60 + exam_minute
time_arrival_in_minutes = arrival_hour * 60 + arrival_minute
condition = ''
text = ''
hh = 0
mm = 0

if time_exam_in_minutes >= time_arrival_in_minutes:
    if time_exam_in_minutes > (time_arrival_in_minutes + 30):
        condition = 'Early'
        if time_exam_in_minutes - time_arrival_in_minutes >= 60:
            if time_exam_in_minutes % time_arrival_in_minutes == 60:
                hh = time_exam_in_minutes // time_arrival_in_minutes
                mm = time_exam_in_minutes % time_arrival_in_minutes - 60
            else:
                hh = (time_exam_in_minutes - time_arrival_in_minutes) // 60
                mm = (time_exam_in_minutes - time_arrival_in_minutes) % 60
            text = f"{hh}:{mm :02d} hours before the start"
        else:
            hh = time_exam_in_minutes // time_arrival_in_minutes
            mm = time_exam_in_minutes % time_arrival_in_minutes
            text = f"{mm} minutes before the start"
    else:
        condition = 'On time'
        mm = time_exam_in_minutes % time_arrival_in_minutes
        text = f"{mm} minutes before the start"
else:
    condition = 'Late'
    if time_arrival_in_minutes - time_exam_in_minutes >= 60:
        if time_arrival_in_minutes % time_exam_in_minutes == 60:
            hh = time_arrival_in_minutes // time_exam_in_minutes
            mm = time_arrival_in_minutes % time_exam_in_minutes - 60
        else:
            hh = (time_arrival_in_minutes - time_exam_in_minutes) // 60
            mm = (time_arrival_in_minutes - time_exam_in_minutes) % 60
        text = f"{hh}:{mm :02d} hours after the start"
    else:
        hh = time_arrival_in_minutes // time_exam_in_minutes
        mm = time_arrival_in_minutes % time_exam_in_minutes
        text = f"{mm} minutes after the start"

print(condition)
print(text)
