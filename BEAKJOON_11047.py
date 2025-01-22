import sys
N,K = map(int,sys.stdin.readline().split())
stack = []
for i in range(N):
    a = int(sys.stdin.readline().strip())
    if a <= K :
        stack.append(a)
stack = sorted(stack,reverse=True)
count = 0
for i in stack:
    if K >= i:
        count += K // i
        K %= i
        if K == 0:
            break
print(count)