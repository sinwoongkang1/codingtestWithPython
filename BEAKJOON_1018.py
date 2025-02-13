import sys

input_board_size_y ,input_board_size_x  = map(int,sys.stdin.readline().strip().split())

original_chess_board = [["B","W","B","W","B","W","B","W"],["W","B","W","B","W","B","W","B"]] * 4
reverse_original_chess_board = [["W","B","W","B","W","B","W","B"],["B","W","B","W","B","W","B","W"]] * 4
chess_board = []

for _ in range(input_board_size_y):
    input_chess_board = str(sys.stdin.readline().strip())
    arr = []
    for i in range(len(input_chess_board)):
        arr.append(input_chess_board[i])
    chess_board.append(arr)


min_differ = []
for c in range(input_board_size_y-8+1):
    for i in range(input_board_size_x-8+1):
        differ = 0
        rev_differ = 0
        a = 0    
        for j in range(8):
            b = 0
            for k in range(i,8+i):
                if chess_board[j+c][k] != original_chess_board[a][b]:
                    differ += 1
                if chess_board[j+c][k] != reverse_original_chess_board[a][b]:
                    rev_differ +=1
                b+=1        
            a+=1
        min_differ.append(differ)
        min_differ.append(rev_differ)

print(min(min_differ))
