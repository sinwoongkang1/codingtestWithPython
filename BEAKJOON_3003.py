whitePieces = list(map(int,input().split()))
blackPieces = [1,1,2,2,2,8]

for i in range(len(blackPieces)):
        blackPieces[i] -= whitePieces[i]
print(*blackPieces)