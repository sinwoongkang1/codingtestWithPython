socreArrays = [list(map(int,input().split())) for _ in range(5)]
score = [ 0 for _ in range(len(socreArrays)) ]
max = 0
count = 0
for i in range(len(socreArrays)) :
    sum = 0
    for j in socreArrays[i]:
        sum += j
    score[i] = sum
    if (score[i]>max):
        max = score[i]
        count = i +1
print(count,max)