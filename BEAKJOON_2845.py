import sys

participants, extent = map(int, sys.stdin.readline().strip().split())
newsPaper = list(map(int, sys.stdin.readline().strip().split()))

for i in range(len(newsPaper)):
    newsPaper[i] = (newsPaper[i] - (participants * extent))

print(*newsPaper,sep=" ")