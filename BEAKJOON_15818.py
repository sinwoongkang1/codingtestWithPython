N,M = map(int,input().split())
inputNum = list(map(int,input().split()))

last = 1
for i in range(len(inputNum)):
    last *= inputNum[i] % M
print(last%M)