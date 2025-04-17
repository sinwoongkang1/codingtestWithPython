import sys

total_price = int(sys.stdin.readline().strip())

book_pirces = 0
for i in range(9):
   book = int(sys.stdin.readline().strip())
   book_pirces += book

print(total_price - book_pirces)
   