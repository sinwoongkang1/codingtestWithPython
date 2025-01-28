import sys

N = int(sys.stdin.readline().strip())
stack = []
for _ in range(N):
   stack.append(int(sys.stdin.readline().strip()))
stack.sort()
for i in stack:
   print(i)