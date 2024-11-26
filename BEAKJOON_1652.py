roomSize = int(input())
roomStructure = [list(map(str,input())) for _ in range(roomSize)]


real_row_count = 0

real_column_count = 0

for i in range(roomSize):
    row_count = 0
    for j in range(roomSize):
        if roomStructure[i][j] ==  ".":
            row_count += 1
        else:
            row_count = 0
        if row_count == 2:
            real_row_count += 1 

for i in range(roomSize):
    column_count = 0
    for j in range(roomSize):
        if roomStructure[j][i] == ".":
            column_count += 1
        else:
            column_count = 0
        if column_count ==2:
            real_column_count += 1


print(real_row_count,real_column_count)