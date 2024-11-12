a,b,c = map(int,input().split())
stack = [a,b,c]
stack.sort()
max = stack[2]
if max >= stack[0]+stack[1] :
    max = (stack[0]+stack[1])-1
print(max+stack[0]+stack[1])