import sys
userInputLine = int(sys.stdin.readline().strip())

stack = []
stack_2 = []
compareArray = []
array = []
brray = []
signal = []

for _ in range(userInputLine):
    userInputNumber = int(sys.stdin.readline().strip())
    stack.append(userInputNumber)
    stack_2.append(userInputNumber)
    compareArray.append(userInputNumber)

compareArray.sort()


while True:
    if len(array) == 0 and len(compareArray) != 0:
        array.append(compareArray[0])
        signal.append("+")
    elif len(compareArray) == 0:
        break
    else:
        if stack[0] != array[-1]:
            array.append(compareArray[0])
            signal.append("+")
    while True:
        if len(array) == 0:
            break
        elif array[-1] == stack[0]:
            brray.append(array[-1])
            if array[-1] in compareArray:
                del compareArray[0]
            del stack[0]
            del array[-1]
            signal.append("-")
        else:
            if array[-1] != stack[0]:
                if array[-1] in compareArray:
                    del compareArray[0]
                break
            else:
                sing = "none"
                break
 
if stack_2 == brray:
    print(*signal,sep="\n")
else:
    print("NO")