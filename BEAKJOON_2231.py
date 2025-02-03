# import sys

# N = str(sys.stdin.readline().strip())
# flag = True

# while flag:
#    for i in range(int(N)):
#       sum = 0
#       i_len = len(str(i))
#       str_i = str(i)
#       for j in range(i_len):
#          sum += int(str_i[j])
#       if i + sum == int(N) :
#          answer = i
#          print(answer)
#          flag = False
#          break

n = int(input()) 

for i in range(1, n+1):  
    num = sum((map(int, str(i))))  
    num_sum = i + num 

    if num_sum == n:
        print(i)
        break
    if i == n: 
        print(0)