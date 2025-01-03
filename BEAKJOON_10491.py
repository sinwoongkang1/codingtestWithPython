import sys
while True:
    try:
        inputLine = sys.stdin.readline().split()
        count = 0

        for i in range(len(inputLine)):
            if "problem" in inputLine[i].upper():
                count += 1
            elif "problem" in inputLine[i].lower():
                count += 1
            else:
                count = count

        if count > 0:
            print("yes")
        else:
            print("no")
    except EOFError : break