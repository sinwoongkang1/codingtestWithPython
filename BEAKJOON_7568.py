import sys

number_of_people = int(sys.stdin.readline().strip())

stack = []
rank = [1] * number_of_people

for _ in range(number_of_people):
    weight,height = map(int,sys.stdin.readline().strip().split())
    stack.append([weight,height])

for i in range(len(stack)):
    for j in range(len(stack)):
        if i == j :
            continue
        else:
            if stack[i][0] < stack[j][0]:
                if stack[i][1] < stack[j][1]:
                   rank[i] += 1
                   
print(*rank,sep=" ")
