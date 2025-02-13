import sys

stack=[]

for _ in range(2):
   voice = str(sys.stdin.readline().strip())
   stack.append(len(voice))

if stack[0] < stack[1]:
   print("no")
else:
   print("go")