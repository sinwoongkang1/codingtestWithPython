inputNum = int(input())
stack_x = []
stack_y = []
for _ in range(inputNum):
    a,b = map(int,input().split())
    stack_x.append(a)
    stack_y.append(b)
length_x = max(stack_x) - min(stack_x)
length_y = max(stack_y) - min(stack_y)
if length_x>0 and length_y>0:
    print(length_x * length_y)
elif length_x ==0 or length_y == 0:
    print(0)
