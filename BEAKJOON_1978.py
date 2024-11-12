import sys
intCount = int(input())
input = sys.stdin.readline().split()
arr = []
stack = []
for i in range(intCount):
    if input[i] != "1" :arr.append(input[i])
    count = 0
    for j in range(1,int(input[i])+1):
        if int(input[i]) % j == 0:
                count +=1
    if count ==2:
        stack.append(input[i])        
print(len(stack))

