participant = int(input())
tShirts_order = list(map(int,input().split()))
T,P = map(int,input().split())

count = 0
for i in tShirts_order:
    if i % T > 0:
        if i // T == 0:
            count += 1
        else :
            count += (i // T) + 1
    elif i % T == 0 :
        count += i // T
   
        
print(count)
print(participant//P, participant % P)