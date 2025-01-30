import sys

N = str(sys.stdin.readline().strip())
flag = True

while flag:
   for i in range(int(N)):
      sum = 0
      i_len = len(str(i))
      str_i = str(i)
      for j in range(i_len):
         sum += int(str_i[j])
      if i + sum == int(N) :
         answer = i
         print(answer)
         flag = False
         break
