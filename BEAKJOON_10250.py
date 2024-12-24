testCase = int(input())
def hotelGuest(a,b,c):
    roomNum = str('101')
    front = roomNum[0]
    back = roomNum[-2:]
    d = c // a
    f = c % a

    if d >0 and f ==0 :
        first = a
        second = d
    else:    
        first =  int(front) + (f - 1)
        second = int(back) + d
        
    if second // 10 == 0:
        print(str(first)+'0'+str(second))
    else:
        print(str(first)+str(second))
for _ in range(testCase):
    a,b,c = map(int,input().split())
    hotelGuest(a,b,c)

    