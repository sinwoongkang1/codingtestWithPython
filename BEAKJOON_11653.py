intCount = int(input())

stack = []
result = []
for i in range(1,intCount+1):
    count = 0
    for j in range(1,intCount+1):
        if i % j == 0:
                count +=1
    if count ==2:
        stack.append(i)
for i in range(len(stack)):
    while intCount > 1:
        if intCount % stack[i] == 0:
            result.append(stack[i])
            intCount //= stack[i]
        elif intCount % stack[i] !=0:
             break    
for i in range(len(result)):
     print(result[i])

