while(True):
    a,b,c = map(int,(input().split()))
    stack = [a,b,c]
    stack.sort()
    if a==b==c==0:
        break
    if stack[2] >= stack[1] + stack[0]: 
        print("Invalid")
    else:
        if a==b==c and not 0:
            print("Equilateral")
        else :
            if a==b or b==c or c==a :
                print("Isosceles")
            else:
                print("Scalene")



   