import sys
inputLine = sys.stdin.readline().split()
number = str(inputLine[0])
signiture = int(inputLine[1])
numSheet = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
result = 0
factor = len(number)-1
for i in range(len(number)):
    result += numSheet.index(number[i]) * (signiture ** factor)
    factor -= 1
print(result)
