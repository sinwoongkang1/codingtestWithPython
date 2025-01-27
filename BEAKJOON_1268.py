import sys

numberOfStudent = int(sys.stdin.readline().strip())

classTable = []
for _ in range(numberOfStudent):
    student_info = list(map(int, sys.stdin.readline().strip().split()))
    classTable.append([[score, 0] for score in student_info])

for i in range(len(classTable[0])):
    for j in range(numberOfStudent-1):
        for k in range(j,numberOfStudent-1):
            if classTable[j][i][0] == classTable[k+1][i][0]:
               classTable[j][i][1] += 1
               classTable[k+1][i][1] += 1
            
stack = []
for i in range(len(classTable[0])):
    sum = 0
    for j in range(numberOfStudent):
        sum += classTable[j][i][1]
    stack.append(sum)
        
print(stack.index(max(stack))+1)
