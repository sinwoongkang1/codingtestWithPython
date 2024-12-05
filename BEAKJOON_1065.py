N = int(input())
M = N
Ncount = 0
while True:
    if M / 10 > 0:
        Ncount += 1
        M = int(M / 10)
    else :
        break
answer = 0
if 0 < N < 10:
    for i in range(1,N+1,1):
        answer += 1
if 9 < N < 100:
    for i in range(1,N+1,1):
        answer += 1
if 99 < N < 1000:
    answer = 99
    for k in range(100,N+1):
        stack = []
        for i in range(Ncount-1,-1,-1):
            Neck =  int( k / (10**i))
            stack.append(Neck)
            k = k - (Neck * (10**i))
        for i in range((len(stack)-2)):
            if stack[i] - stack[i+1] == stack[i+1] - stack[i+2]:
                answer += 1
if N == 1000:
    answer = 144
print(answer)
