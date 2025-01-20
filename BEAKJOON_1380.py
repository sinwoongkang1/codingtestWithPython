import sys
answer = []
while True:
    arr = []
    testCase = int(sys.stdin.readline().strip())
    if testCase == 0:
        break
    else:
        for i in range(testCase):
            name = str(sys.stdin.readline().strip())
            arr.append([name,0])
        for i in range(2*testCase -1):
            a ,b = map(str,sys.stdin.readline().split())
            a = int(a)            
            if arr[a-1][1] == 0:
                arr[a-1][1] = b
            else:
                if arr[a-1][1] != 0 and arr[a-1][1] != b:
                  arr[a-1][1] = 1
        for i in range(len(arr)):
            if arr[i][1] != 1:
                answer.append(arr[i][0])
for i in range(len(answer)):
    print(i+1,answer[i])
        


       
      