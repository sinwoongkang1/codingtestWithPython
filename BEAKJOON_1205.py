import sys

N,score,P= map(int,(sys.stdin.readline().split()))
if N > 0:
    socreList = list(map(int,sys.stdin.readline().split()))
answer = 0

if N == P :
    if min(socreList) >= score:
        answer = -1
    else:
        socreList.sort(reverse=True)
        socreList.pop()
        socreList.append(score)
        socreList.sort(reverse=True)
        answer = socreList.index(score) + 1
elif N == 0 :
    answer = 1

else:
    socreList.append(score)
    socreList.sort(reverse=True)
    answer = socreList.index(score) +1

print(answer)