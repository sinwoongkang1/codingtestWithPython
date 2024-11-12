testCount = int(input())
two = [2,4,8,6]
three = [3,9,7,1]
four = [4,6]
seven = [7,9,3,1]
eight = [8,4,2,6]
nine= [9,1]
for _ in range(testCount):
    a,b = map(int,input().split())
    a = a%10
    if a==0:
       print(10)
    elif a == 1 or a==5 or a==6 :
       print(a)
    elif a==2 :
       b %= 4
       print(two[b-1])
    elif a==3 :
       b %= 4
       print(three[b-1])
    elif a==7 :
       b %= 4
       print(seven[b-1])
    elif a==8 :
       b %= 4
       print(eight[b-1])
    elif a ==4 :
       b %= 2
       print(four[b-1])
    elif a ==9 :
       b %= 2
       print(nine[b-1])