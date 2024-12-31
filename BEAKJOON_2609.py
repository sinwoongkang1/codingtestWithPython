a,b = map(int,input().split())
c = a
d = b
while b != 0 :
    a,b = b, a%b
    
print(a)
print((c*d)//a)