import sys
flag = True

while flag:
    a = float(sys.stdin.readline().strip())
    if a == 0:
        flag = False
        break
    else:
        print("{:.2f}".format(1 + (a) + (a**2) + (a**3) + (a**4)))