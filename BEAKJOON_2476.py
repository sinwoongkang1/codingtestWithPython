poepleNum = int(input())
winnerMoney = 0
for _ in range(poepleNum):
    a,b,c, = map(int,input().split())
    if a==b==c:
        award = 10000+a*1000
    elif a!=b and b!=c and c!=a:
        award = max(a,b,c)*100    
    elif a==b!=c or b==c!=a or c==a!=b :
        if a==b:
            award = 1000+a*100
        if b==c:
            award = 1000+b*100
        if c==a:
            award = 1000+c*100
    if award >= winnerMoney:
        winnerMoney = award
print(winnerMoney)