roomSize = int(input())
roomStructure = [list(map(str,input())) for _ in range(roomSize)]

row_count = [False]*roomSize
column_count = [False]*roomSize

for i in range(roomSize):
    for j in range(roomSize-1):
        if roomStructure[i][j] ==  ".":
            if roomStructure[i][j+1] == ".":
                row_count[i] = True

for i in range(roomSize):
    for j in range(roomSize-1):
        if roomStructure[j][i] == ".":
            if roomStructure[j+1][i] == ".":
                column_count[i] = True

def makeCount(data):
    count = 0
    for i in data:
        if i == True:
            count += 1
    return count

answer = []
answer.append(makeCount(row_count))
answer.append(makeCount(column_count))
print(*answer,sep=" ")