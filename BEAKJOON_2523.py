N = int(input())
for i in range(1,2*N):
    if i <= N :
        print("*"* int(i)) 
    elif i > N:
        print("*"* int(2*N-i)) 