import sys

N = int(sys.stdin.readline().strip())

sum = 1
for i in range(1,N+1):
   sum *= i

targetNum = str(sum)
count = 0

for i in range(len(targetNum)-1,-1,-1):
    if '0' == targetNum[i]:
        count += 1
    else:
        break
print(targetNum)
print(count)