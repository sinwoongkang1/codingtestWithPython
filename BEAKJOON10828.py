import sys

commandLineCounter = int(input())
stack = []
for _ in range(commandLineCounter):
    command = sys.stdin.readline().split()
    if(command[0] == "push"):
        stack.append(command[1])
    elif(command[0] == "pop"):
        if(len(stack)>0):
            print(stack[len(stack)-1])
            stack.pop(len(stack)-1)
        else:
            print(-1)
    elif(command[0] =="size"):
        print(len(stack))
    elif(command[0] =='empty'):
        if(len(stack)>0):
            print(0)
        else : 
            print(1)
    elif(command[0] == "top"):
        if(len(stack)==0):
            print(-1)
        else:
            print(stack[len(stack)-1])

