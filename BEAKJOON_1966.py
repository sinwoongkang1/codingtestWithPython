docCount, printDoc = map(int,input().split())
primaryCount = list(map(int,input().split()))
order = docCount - printDoc

flag = True
while flag:
    for i in range(docCount):
        temp = []
        firstPrintOrder = primaryCount[-1]
        if firstPrintOrder < primaryCount[i]:
            primaryCount.pop()
            temp.append(firstPrintOrder)
            temp.extend(primaryCount)
            primaryCount = temp
            order -= 1
        else:
            if firstPrintOrder == max(primaryCount):
                flag = False
                break
print(order)
