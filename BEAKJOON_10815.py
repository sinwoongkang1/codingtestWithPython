firstNum= int(input())
firstArray = set(map(int,input().split()))
secondNum= int(input())
secondArray = list(map(int,input().split()))
checkArray = []
for i in secondArray:
    if i in firstArray:   
        checkArray.append(1)
    else:
        checkArray.append(0)
print(*checkArray,sep=" ")

