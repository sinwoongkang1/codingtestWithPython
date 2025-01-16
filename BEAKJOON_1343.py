import sys

exampleInput = str(sys.stdin.readline().strip())

board = exampleInput.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if "X" in board:
    print("-1")
else:
    print(board)