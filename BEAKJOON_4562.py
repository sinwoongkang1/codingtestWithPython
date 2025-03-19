import sys

test_case = int(sys.stdin.readline().strip())
for i in range(test_case):
    x,y = map(int, sys.stdin.readline().strip().split())
    if x >= y:
        print("MMM BRAINS")
    else:
        print("NO BRAINS")