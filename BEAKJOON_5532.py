import sys

stack=[]

for _ in range(5):
    a = sys.stdin.readline().strip()
    stack.append(int(a))

count = 1
flag = True

while flag:
    if stack[1] <= (stack[3] * count):
        if stack[2] <= (stack[4] * count):
            flag = False
            break
        else:
            count += 1
    else:
        count += 1
print(stack[0]-count)