numberOfInput = int(input())
stack = []
for _ in range(numberOfInput):
    a = input()
    stack.append(a)
setStack  = set(stack)
stack = list(setStack)
stack.sort()
stack.sort(key=len)
for i in stack:
    print(i)