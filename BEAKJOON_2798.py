import sys , itertools
cardCount, maxNum = map(int,input().split())
input = sys.stdin.readline().split()
answer = 0
stack = []
for i in range(cardCount):
    stack.append(int(input[i]))
selectNums = itertools.combinations(stack,3)
for i in selectNums:
    if sum(i) <= maxNum :
        answer = max(answer,sum(i))
print(answer)
itertools.isl