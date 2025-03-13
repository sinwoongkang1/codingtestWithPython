import sys

employee_1 = list(map(int, sys.stdin.readline().strip().split()))
employee_2 = list(map(int, sys.stdin.readline().strip().split()))
employee_3 = list(map(int, sys.stdin.readline().strip().split()))

def workingTime(employee):

    time = employee[3] - employee[0]

    second = employee[5] - employee[2]

    if second < 0 :
        second = (employee[5]+60) - employee[2]
        employee[4] -= 1

    minute = employee[4] - employee[1]

    if employee[4] < employee[1] :
        time -= 1
        minute = (60+ employee[4]) - employee[1]


    return print(time, minute, second)

workingTime(employee_1)
workingTime(employee_2)
workingTime(employee_3)