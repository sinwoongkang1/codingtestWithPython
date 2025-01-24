import sys
a,b,c = map(int,sys.stdin.readline().strip().split())
a= str(a/b)
target = a.split(".")
letter = target[1]
print(letter[c-1:c+1])
