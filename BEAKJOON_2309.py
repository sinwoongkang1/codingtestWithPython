import sys
number_of_questions = int(sys.stdin.readline().strip())
get_points = list(sys.stdin.readline().strip().split())
result = []
for i in range(number_of_questions):
    count = 1
    if i == 0:
        if get_points[i] == '1':
            result.append(count)
        else:
            result.append(0)
    else:
        if get_points[i-1] == '1':
            if get_points[i] == '1':
                result.append((result[i-1])+1)
            else :
                result.append(0)
        else:
            if get_points[i-1] == '0':
                if get_points[i] == '1':
                    result.append(1)
                else:
                    count = 0
                    result.append(count)
print(sum(result))
