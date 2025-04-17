import sys

test_case = int(sys.stdin.readline().strip())

for i in range(test_case):
    stack = []
    user_input = sys.stdin.readline().strip()
    for j in range(len(user_input)):
        if len(stack) == 0:
            stack.append(user_input[j])
        else:
            if user_input[j-1] != user_input[j] :
                stack.append(user_input[j])
    print(*stack,sep="")