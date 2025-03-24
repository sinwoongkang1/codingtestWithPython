import sys

word = sys.stdin.readline().strip()
count = [0] * 26

for i in word:
    if i == "a":
        count[0] +=1
    elif i == "b":
        count[1] +=1
    elif i == "c":
        count[2] +=1
    elif i == "d":
        count[3] +=1
    elif i == "e":
        count[4] +=1
    elif i == "f":
        count[5] +=1
    elif i == "g":
        count[6] +=1
    elif i == "h":
        count[7] +=1
    elif i == "i":
        count[8] +=1
    elif i == "j":
        count[9] +=1
    elif i == "k":
        count[10] +=1
    elif i == "l":
        count[11] +=1
    elif i == "m":
        count[12] +=1
    elif i == "n":
        count[13] +=1
    elif i == "o":
        count[14] +=1
    elif i == "p":
        count[15] +=1
    elif i == "q":
        count[16] +=1
    elif i == "r":
        count[17] +=1
    elif i == "s":
        count[18] +=1
    elif i == "t":
        count[19] +=1
    elif i == "u":
        count[20] +=1
    elif i == "v":
        count[21] +=1
    elif i == "w":
        count[22] +=1
    elif i == "x":
        count[23] +=1
    elif i == "y":
        count[24] +=1
    elif i == "z":
        count[25] +=1

print(*count,sep=" ")


