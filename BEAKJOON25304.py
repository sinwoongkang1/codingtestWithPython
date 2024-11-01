totalPrice = int(input())
itemsCount = int(input())
realTotalPrice = 0
for _ in range(itemsCount):
    price,ea=map(int,input().split())
    realTotalPrice += price*ea
if(totalPrice==realTotalPrice):
    print("Yes")
else:
    print("No")