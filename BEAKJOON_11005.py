number, signiture = map(int, input().split())
numSheet = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
            "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
            "U", "V", "W", "X", "Y", "Z"]
result = []
if number == 0:
    result.append(numSheet[0])  
while number > 0:
    nature = number % signiture
    result.append(numSheet[nature])
    number = int(number/signiture)

print(*result[::-1], sep='')