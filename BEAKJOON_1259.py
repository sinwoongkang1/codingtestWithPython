while (True):
    inputNumber = str(input())
    if inputNumber == "0":
        break
    else:    
        center = int(len(inputNumber) / 2)
        count = 0
        for i in range(center):
            if inputNumber[i] == inputNumber[i+(-1-(2*i))]:
                count+=1
        if center == count:
            print("yes")
        else :
            print("no")