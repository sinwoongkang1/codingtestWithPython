import sys

N = int(sys.stdin.readline().strip())
stack = []

for i in range(1,N+1):
    if i > 0:
        stack.append(i)
        if i % 6 == 0 :
            stack.append("Go!")

if stack[-1] == "Go!":
    print(*stack,sep=" ")
else:
    stack.append("Go!")
    print(*stack,sep=" ")
