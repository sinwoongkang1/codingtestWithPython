import sys

month = int(sys.stdin.readline().strip())
day = int(sys.stdin.readline().strip())

if month < 2:
    print("Before")
else:
    if month == 2:
        if day < 18:
            print("Before")
        elif day >18:
            print("After")
        elif day == 18:
            print("Special")
    else:
        if month > 2:
            print("After")