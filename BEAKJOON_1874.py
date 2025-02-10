import sys
userInputLine = int(sys.stdin.readline().strip())

stack = []
compareArray = []
array = []
brray = []

for _ in range(userInputLine):
    userInputNumber = int(sys.stdin.readline().strip())
    stack.append(userInputNumber)
    compareArray.append(userInputNumber)

compareArray.sort()


while True:
    sing = None
    if len(array) == 0:
        array.append(compareArray[0])
    else:
        if stack[0] != array[-1]:
            array.append(compareArray[0])
    if array[-1] == stack[0]:
        brray.append(array[-1])
        del compareArray[0]
        del stack[0]
        del array[-1]
        sign = "+"
    else:
        if array[-1] != stack[0]:
            sign = "+"
            del compareArray[0]
        else:
            sing = "none"
    if sing == "none":
        break
    else:
        print(sign)



