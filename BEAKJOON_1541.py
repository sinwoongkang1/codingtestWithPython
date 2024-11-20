string = input().split("-")
answer = 0
sum = 0
for i in string[0].split("+"):
    answer += int(i)
for i in string[1:]:
    for j in i.split("+"):
        sum += int(j)
print(answer-sum)