import sys

input_Numbers = list(map(int,sys.stdin.readline().strip().split()))

sorted_input_Numbers = sorted(input_Numbers)

print(*sorted_input_Numbers,sep=' ')