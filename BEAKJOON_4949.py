import sys

while True:
    inputLine = list(map(str,sys.stdin.readline().split()))

    if inputLine[0] == ".":
        break
    else:
        small = []
        big = []
        for i in inputLine:
            if "(" in i :
               small.append("(")
            if ")" in i :
               small.append(")")
            if "[" in i :
               big.append("[")
            if "]" in i :
               big.append("]")
        if len(small) %2 ==0 :
            if len(big) %2 == 0:
                count = 0
                for i in range(0,len(small),+2):
                    if small[i] == "(":
                        count += 1
                for i in range(1,len(small),+2):
                    if small[i] ==")":
                        count += 1
                if len(small) == count:
                    count = 0
                for i in range(0,len(big),+2):
                    if big[i] == "[":
                        count += 1
                for i in range(1,len(big),+2):
                    if big[i] =="]":
                        count += 1
                if len(big) == count:
                    count = 0
                if count == 0:
                    print("yes")
                else:
                    print("no")
