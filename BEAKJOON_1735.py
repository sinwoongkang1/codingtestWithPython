import math
a,b = map(int,input().split())
c,d = map(int,input().split())
a = (a*d)+(c*b)
b = (b*d)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)
result = gcd(a,b)
if gcd(a,b) > 0 :
    a //= result
    b //= result
print(a,b)
