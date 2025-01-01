N = int(input())
array = [[0] * 100 for _ in range(100)]
count = 0
for i in range(N):
    a,b = map(int,input().split())
    for j in range(a,a+10,1):
        for k in range(b,b+10,1):
            if array[j][k] == 0 :
                array[j][k] = 1
                count += 1
print(count)







