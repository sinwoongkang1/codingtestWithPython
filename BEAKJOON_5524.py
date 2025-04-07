import sys

test_case = int(sys.stdin.readline().strip())
stack = []



for i in range(test_case):
    Si = sys.stdin.readline().strip()
    stack.append(Si.lower())

print(*stack, sep='\n')

