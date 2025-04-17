import sys
flag = True

while flag:
    a = float(sys.stdin.readline().strip())
    if a < 0:
        flag = False
        break
    else:
        b = round(a * 0.167,3)
        text = "Objects weighing {:.2f} on Earth will weigh {:.2f} on the moon.".format(a,b)
        print(text)
