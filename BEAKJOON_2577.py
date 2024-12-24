A = int(input())
B = int(input())
C = int(input())
D = A * B * C 
array = [0]*10

D=str(D)
for i in range(len(D)):
    a = int(D[i])
    array[a] += 1

for i in array:
    print(i)