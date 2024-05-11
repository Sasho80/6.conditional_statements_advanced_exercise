hour_exam = int(input())
minute_exam = int(input())
hour_arrival = int(input())
minute_arrival = int(input())

HOUR = 60
HALF_HOUR = 30

sum_hour_minutes_exam = hour_exam * HOUR + minute_exam
sum_hour_minutes_arrival = hour_arrival * HOUR + minute_arrival
diff_hours_minutes_exam_arrival = sum_hour_minutes_exam - sum_hour_minutes_arrival

if 0 > diff_hours_minutes_exam_arrival > -60:
    diff_hours_minutes_exam_arrival = abs(diff_hours_minutes_exam_arrival)
    print("Late")
    print(f"{diff_hours_minutes_exam_arrival} minutes after the start")
    exit()
elif diff_hours_minutes_exam_arrival <= -60:
    diff_hours_minutes_exam_arrival = abs(diff_hours_minutes_exam_arrival)
    if diff_hours_minutes_exam_arrival % 60 <= 9:

        print("Late")
        print(f"{diff_hours_minutes_exam_arrival // 60}:0{diff_hours_minutes_exam_arrival % 60}"
              f"hours after the start")
        exit()
    else:
        print("Late")
        print(f"{diff_hours_minutes_exam_arrival // 60}:{diff_hours_minutes_exam_arrival % 60}"
              f" hours after the start")
        exit()
elif diff_hours_minutes_exam_arrival == 0:
    print("On time ")
    exit()
elif 0 < diff_hours_minutes_exam_arrival <= 30:
    print("On time ")
    print(f"{diff_hours_minutes_exam_arrival} minutes before the start")
elif 30 < diff_hours_minutes_exam_arrival < 60:
    print("Early ")
    print(f"{diff_hours_minutes_exam_arrival} minutes before the start")
elif diff_hours_minutes_exam_arrival >= 60:
    if diff_hours_minutes_exam_arrival % 60 <= 9:
        print("Early")
        print(f"{diff_hours_minutes_exam_arrival // 60}:0{diff_hours_minutes_exam_arrival % 60} hours before the start")
    else:
        print("Early")
        print(f"{diff_hours_minutes_exam_arrival // 60}:{diff_hours_minutes_exam_arrival % 60} hours before the start")
        exit()
