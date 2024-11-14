row,lengh = map(int,input().split())
castleData = [list(map(str,input())) for _ in range(row)]
x_guard = 0
y_guard = 0
for i in range(row):
    dotCount = 0
    for j in range(lengh):   
        if castleData[i][j] == ".":
            dotCount += 1
    if dotCount == lengh:
        x_guard += 1           
for i in range(lengh):
    dotCount = 0
    for j in range(row):   
        if castleData[j][i] == ".":
            dotCount += 1
    if dotCount == row:
        y_guard += 1
print(max(x_guard,y_guard))
                