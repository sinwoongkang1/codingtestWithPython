while True:
    firstNumber = int(input())
    if firstNumber == 0:
        break
    secondNum = firstNumber *2

    printNumber = []
    for i in range(secondNum+1):
        printNumber.append(i)

    is_sosu = [True]*(secondNum+1)
    is_sosu[0] = is_sosu[1] = False

    for i in range(2,secondNum+1):
        if is_sosu[i]:
            for j in range(i*i,secondNum+1,i):
                is_sosu[j] = False
    count = 0
    for i in printNumber:
        if is_sosu[i] == True:
            if firstNumber < printNumber[i] <= secondNum:
                count += 1
    print(count)