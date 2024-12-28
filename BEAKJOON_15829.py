lenOfalphabet = int(input())
alphabetLine = input()
count = 0
for i in range(len(alphabetLine)):
    count += ((ord(alphabetLine[i])-96) * (31 ** i))
print(count)

import math

# n과 k 설정
n = 5
k = 2

# 조합의 수 계산
combinations = math.comb(n, k)