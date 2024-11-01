while(True):
    a,b=map(int,input().split())
    if(a<b and b%a==0):
        print("factor")
    elif(a>b and a%b==0):
        print("multiple")
    elif(a<b and b%a!=0 or a>b and a%b!=0):
        print("neither")
    elif(a==0 & b==0):
        break