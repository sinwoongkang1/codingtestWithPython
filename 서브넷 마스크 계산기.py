import sys

userInput = sys.stdin.readline().strip()

if "/" in userInput:
    ipAddress = list(map(int, userInput.split("/")[0].split(".")))
    subnetMask = int(userInput.split("/")[1]) 
    ipAddress.append(subnetMask) 
else:
    ipAddress = list(map(int,userInput.split(".")))

print(ipAddress)

classAsubNet = [11111111,00000000,00000000,00000000]
classBsubNet = [11111111,11111111,00000000,00000000]
classCsubNet = [11111111,11111111,11111111,00000000]

def makeNumber10to2(number):
    stack = []
    while number > 0:
        stack.append(number % 2)
        number //= 2

    if len(stack) < 8:
        zero = [0] * (8 - len(stack))
        stack.extend(zero)

    return stack[::-1]

if len(ipAddress) > 4 :
    makeSubnet = [00000000,00000000,00000000,00000000]
else:
    if ipAddress[0] <= 127:
        for i in ipAddress:
            newAddress = []
            newAddress.append(makeNumber10to2(i))
        print(newAddress)
    elif ipAddress[0] <=191:
        for i in ipAddress:
            newAddress = []
            newAddress.append(makeNumber10to2(i))
        print(newAddress)
    else:
        for i in ipAddress:
            newAddress = []
            newAddress.append(makeNumber10to2(i))
        print(newAddress)