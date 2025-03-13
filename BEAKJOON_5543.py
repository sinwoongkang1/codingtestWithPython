import sys
burgers = []
for _ in range(3):
    burgers.append(int(sys.stdin.readline().strip()))
beverages = []
for _ in range(2):
    beverages.append(int(sys.stdin.readline().strip()))
print(min(burgers)+min(beverages)-50)

