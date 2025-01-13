import sys

testCase = int(sys.stdin.readline())

def viewPrintSum(number):
    stack = [1,2,4]
    for i in range(3,number):
        stack.append(stack[i-3] + stack[i-2]+ stack[i-1])
    return stack[number-1]

for _ in range(testCase):
    print(viewPrintSum(int(sys.stdin.readline())))
