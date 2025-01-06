numOfN = int(input())
arrayOfN = set(map(int,input().split()))
numOfM= int(input())
arrayOfM = list(map(int,input().split()))
answer = []

for i in arrayOfM :
    if i in arrayOfN :
        print(1)
    else:
        print(0)

