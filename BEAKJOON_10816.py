import sys

N = int(input())
numberCard = list(map(int,sys.stdin.readline().split()))
M = int(input())
myCard = list(map(int,sys.stdin.readline().split()))

count = {}
for card in numberCard:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for target in myCard:
    result = count.get(target)
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")