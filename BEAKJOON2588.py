number1 = int(input())
number2 = list(map(int,input()))
sum = 0
j = 0
for i in range(len(number2)-1,-1,-1) :
    result = number1 * number2[i]
    print(result)
    sum += int((result*(10**(j))))
    j+=1
print(int(sum))