givenNumber = int(input())
count = 0
targetNum = givenNumber
while True:
    a = int(targetNum / 10)
    b = targetNum % 10
    c= a+b
    targetNum = (b * 10) + (c % 10)
    count += 1
    if targetNum == givenNumber:
        break
print(count)