import sys

flag = True

while flag:
    name, age, weight = map(str, sys.stdin.readline().strip().split())
    if name == "#" or age == "0" or weight == "0":
        flag = False
        break
    else:
        if age > "17" or weight >= "80":
            print(name, "Senior")
        else:
            print(name, "Junior")
