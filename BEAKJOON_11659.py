import sys

N,M = sys.stdin.readline().strip().split()
inputNumbers = list(sys.stdin.readline().strip().split())
sum = 0
sumArr = [0]
for i in inputNumbers:
   sum += int(i)
   sumArr.append(sum)

for _ in range(int(M)):
   first,end = sys.stdin.readline().strip().split()
   print(sumArr[int(end)] - sumArr[int(first)-1])
