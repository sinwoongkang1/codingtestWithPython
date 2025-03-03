import sys

score_1 = list(map(int,sys.stdin.readline().strip().split()))
score_2 = list(map(int,sys.stdin.readline().strip().split()))
print(max(sum(score_1),sum(score_2)))