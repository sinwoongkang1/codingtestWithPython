testCase = int(input())
def find (a,b):
    while b!= 0:
        a,b = b , a % b
    return abs(a)
for _ in range(testCase):
    a,b = map(int,input().split())
    c = find(a,b)
    answer = (a*b) // c
    print(answer) 

