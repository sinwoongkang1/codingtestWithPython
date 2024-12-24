a,b,c,d,e = map(int,input().split())


def makeNumber(a,b,c,d,e):
    a = a* a
    b = b* b
    c = c* c
    d = d* d
    e = e* e
    f = a+b+c+d+e
    print(f%10)


makeNumber(a,b,c,d,e)