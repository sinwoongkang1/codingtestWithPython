N = int(input())
array = (list(map(int,input().split())))
S = int(input())

while S != 0:
    for i in range(N-1):
        temp = 0
        if array[i] < array[i+1]:
            temp = array[i]
            array[i] = array[i+1]
            array[i+1] = temp
            S -= 1
            if S == 0:
                break
print(*array,sep=" ")