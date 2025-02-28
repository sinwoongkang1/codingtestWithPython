import sys

time, minute, second = map(int,sys.stdin.readline().strip().split())
total_second = int(sys.stdin.readline().strip())

def clock(user_time, user_minute, user_second):
    if user_second>=60:
        user_minute += user_second // 60
        user_second %= 60
    if user_minute>=60:
        user_time += user_minute // 60
        user_minute %= 60
    if user_time >= 24:
        user_time %= 24
    print(user_time,user_minute,user_second)

if total_second >= 3600:
    time += total_second // 3600
    last_minute = total_second % 3600
    if last_minute >= 60:
        minute += last_minute // 60
        second += last_minute % 60
    else:
        second += last_minute
else:
    if total_second >= 60:
        minute += total_second // 60
        second += total_second % 60
    else:
        second += total_second

clock(time,minute,second)