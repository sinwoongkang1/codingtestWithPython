flag = int(input())
while flag != 0:
    result = str(input())
    count = 0
    stack = []
    resultStack = []
    for i in range(len(result)):
        if result[i] == "O":
            stack.append(1)
            resultStack.append(1)
        else:
            stack.append(0)
            resultStack.append(0)
    for i in range(1,len(stack)):
        if stack[i] == stack[i-1]:
            resultStack[i] = resultStack[i] + resultStack[i-1]
    for i in resultStack:
        count += i
    print(count)
    flag -=1