numberOfSeat = int(input())
seatInfo = str(input())
cupholder = 1

stack = []
for i in range(len(seatInfo)):
    stack.append(seatInfo[i])

for _ in range(len(stack)):
    if len(stack) == 0:
        break
    elif stack[0] == "S":
        cupholder += 1
        stack.remove(stack[0])
    elif stack[0] =="L":
        if stack[1] == "L":
            cupholder += 1
            stack.remove(stack[0])
            stack.remove(stack[0])

if cupholder >= numberOfSeat:
    print(numberOfSeat)
elif cupholder < numberOfSeat:
    print(cupholder)