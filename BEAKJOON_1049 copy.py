import sys
flag = True

while flag:
    a,b = map(int,sys.stdin.readline().strip().split())
    if a > b:
        print("Yes")
    else:
        if a == 0 and b == 0 :
            flag = False
            break
        elif a <= b:
            print("No")
