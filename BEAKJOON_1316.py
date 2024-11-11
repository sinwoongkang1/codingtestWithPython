import sys
total = 0
sumCount = 0

for _ in range(20):
    input = sys.stdin.readline().split()
    time = float(input[1])
    grade = str(input[2])
    if grade == "A+":
        total += (4.5 * time)
        sumCount += time
    elif grade == "A0":
        total += (4 * time)
        sumCount += time
    elif grade == "B+":
        total += (3.5 * time)
        sumCount += time
    elif grade == "B0":
        total += (3 * time)
        sumCount += time
    elif grade == "C+":
        total += (2.5 * time)
        sumCount += time
    elif grade == "C0":
        total += (2 * time)
        sumCount += time
    elif grade == "D+":
        total += (1.5 * time)
        sumCount += time
    elif grade == "D0":
        total += (1 * time)
        sumCount += time
    elif grade == "F":
        sumCount += time
print(total/sumCount)
    
