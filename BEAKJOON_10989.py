N = int(input())
stack = []
for _ in range(N):
    a = int(input())
    stack.append(a)
stack.sort()
for i in stack:
    print(i)