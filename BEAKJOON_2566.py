inputArray = [list(map(int,input().split())) for _ in range(9)]
maxCount = 0
max_x = 0
max_y = 0
for i in range(len(inputArray)):
    for j in range (len(inputArray)):
        if inputArray[i][j] > maxCount:
            maxCount = inputArray[i][j]
            max_x = i
            max_y = j
print(maxCount)
print(max_x+1,max_y+1)