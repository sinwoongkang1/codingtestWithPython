firstNum= int(input())
secondNum= int(input())
stack = []
sum=0
for i in range(firstNum,secondNum+1):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count +=1
    if count ==2:
        stack.append(i)
        sum += i
if len(stack)==0:
    print(-1)
else:
    print(sum)
    print(min(stack))

