int_K = int(input())
stack = []
for _ in range(int_K):
    inputNumber = int(input())
    stack.append(inputNumber)
    if inputNumber == 0:
        stack.pop()
        stack.pop()
print(sum(stack))
