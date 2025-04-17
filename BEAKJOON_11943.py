import sys

a,b = map(int,sys.stdin.readline().strip().split())
c,d = map(int,sys.stdin.readline().strip().split())

count = min(a+d,b+c)
print(count)