import sys
K,N,M = map(int,sys.stdin.readline().strip().split())
money = K*N-M
if money >= 0:
    print(K*N-M)
else:
    print(0)