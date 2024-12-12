numberOfInput = int(input())
stack = []
for _ in range(numberOfInput):
    a = input()
    stack.append(a)
stack.sort(key=len)
stack.sort
print(stack)
newStack = list(set(stack))
print(newStack)