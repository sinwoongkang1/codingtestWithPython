sentence = input()
sentenceArray = []
for i in range(len(sentence)):
    sentenceArray.append(sentence[i])

for i in range(len(sentenceArray)):
    if sentenceArray[i].isupper():
        sentenceArray[i] = sentenceArray[i].lower()
    elif sentenceArray[i].islower():
        sentenceArray[i] = sentenceArray[i].upper()

print(*sentenceArray,sep="")