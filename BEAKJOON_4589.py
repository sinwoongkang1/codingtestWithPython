import sys

test_cases = int(sys.stdin.readline().strip())
stack = []
for case in range(test_cases):
    a,b,c, = map(int, sys.stdin.readline().strip().split())
    if a < b:
        if b < c:
            stack.append("Ordered")
        else:
            stack.append("Unordered")
    if a > b :
        if b > c :
            stack.append("Ordered")
        else:
            stack.append("Unordered")
print("Gnomes:")
print(*stack,sep="\n")