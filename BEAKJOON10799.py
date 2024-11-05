customerInput = input()
stack = []
count = 0
for i in range(len(customerInput)):
    if customerInput[i] == "(" :
        stack.append(customerInput[i])
    else:
        if customerInput[i-1] == "(":
            stack.pop()
            count+=len(stack)
        else :
            stack.pop()
            count += 1
print(count)