N = int(input())
arr = []
for _ in range(N):
    a,b = map(int,input().split())
    arr.append([a,b])
arr.sort()

for i in arr:
    print(i[0],i[1])