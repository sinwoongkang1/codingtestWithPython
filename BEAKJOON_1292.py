a,b = map(int,input().split())
def sliceSum(data,num1,num2):
    sum = 0
    for i in data[num1-1:num2]:
        sum += i
    return sum
stack = []
for i in range(1,b+1):
    for j in range(i):
        if len(stack)<=b:    
            stack.append(i)
        else:
            break
a = sliceSum(stack,a,b)
print(a)