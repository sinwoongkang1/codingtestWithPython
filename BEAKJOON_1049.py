breakLine, brandCount = map(int,input().split())

priceOfPackageStack = []
priceOfEachStack = []
for _ in range(brandCount):
    priceOfPackage, priceOfEach = map(int,input().split())
    priceOfPackageStack.append(priceOfPackage)
    priceOfEachStack.append(priceOfEach)
    
a = breakLine * min(priceOfEachStack)

b =(int(breakLine/6) + 1) * min(priceOfPackageStack)

c = ( int(breakLine/6) * min(priceOfPackageStack) ) + (breakLine % 6) * min(priceOfEachStack)

print(min(a,b,c))

