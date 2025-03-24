import sys
day = int(sys.stdin.readline().strip())
cars = list(map(int, sys.stdin.readline().strip().split()))
count = 0
for i in cars:
    if day == i:
        count += 1
print(count)