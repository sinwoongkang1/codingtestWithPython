N = int(input())
count = N
for i in range(count):
    inputWord = str(input())
    for j in range(len(inputWord)-1):
        if inputWord[j] == inputWord[j+1]:
            continue
        if inputWord[j] in inputWord[j+1:]:
            count -= 1
            break
print(count)
