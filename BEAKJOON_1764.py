import sys
a,b = map(int,sys.stdin.readline().split())
notListen = set()
notLook = set()
for _ in range(a):
    notListen.add(input())
for _ in range(b):
    notLook.add(input())

count = 0
notListenLook = []
for i in notListen:
    if i in notLook:
        count += 1
        notListenLook.append(i)
notListenLook.sort()
print(count)
for i in notListenLook:
    print(i)