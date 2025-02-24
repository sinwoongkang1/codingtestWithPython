import sys

numberCount = int(sys.stdin.readline().strip())
inputNumbers = list(map(int,sys.stdin.readline().strip().split()))

map = {}

sortedNumbers = sorted(inputNumbers)

count = 0
for i in sortedNumbers:
    if i not in map:
        map[i] = count
        count += 1

stack = []
for i in inputNumbers:
    stack.append(map[i])

print(*stack,sep=' ')