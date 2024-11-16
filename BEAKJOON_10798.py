import sys
input = [list(sys.stdin.readline().strip()) for _ in range(5)]
stack = []
for i in range(15):
    for j in range(5):
        if i < len(input[j]):
            stack.append(input[j][i])
print(*stack,sep='')
