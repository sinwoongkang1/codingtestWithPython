testCount = int(input())
for _ in range(testCount):
    roomCount = int(input())
    def countExistPeople(data):
        roomState = [False]*data
        for i in range(1,data+1):
            for j in range(1,data+1):
                if j%i ==0:
                    if roomState[j-1] == True:
                        roomState[j-1] = False
                    elif roomState[j-1] == False:
                        roomState[j-1] = True
        count = 0
        for i in roomState:
            if i == True:
                count += 1
        return count
    print(countExistPeople(roomCount))