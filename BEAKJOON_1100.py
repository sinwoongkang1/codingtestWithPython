chessTable = [list(map(str,input())) for _ in range(8)]
count = 0
for i in range(0,8):
    if i ==0 or i%2 == 0:
        for j in range(0,8,2):
            if chessTable[i][j] == "F":
                count += 1
    elif i % 2 != 0:
        for k in range(1,9,2):
            if chessTable[i][k] == "F":
                count += 1
print(count)