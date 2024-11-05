integerCount = int(input())
numList = list(map(int,input().split()))
numList.sort()
print(numList[0],numList[integerCount-1])
