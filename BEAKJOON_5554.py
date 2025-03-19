import sys
sum = 0
for _ in range(4):
    a = sys.stdin.readline().strip()
    sum += int(a)

minute = sum//60
second = sum%60
print(minute)
print(second)