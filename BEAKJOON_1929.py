firstNum,secondNum = map(int,input().split())

# stack = []
# sosu = []
# for i in range(1,secondNum+1):
#     stack.append(i)
# for i in range(1,secondNum+1):
#     count = []
#     for j in stack:
#         if i % j == 0:
#             count.append(j)
#         elif j > i:
#             break
#         elif len(count) > 2:
#             break
#     if len(count) == 2:
#         sosu.append(i)
# for i in sosu:
#     if firstNum <= i <= secondNum:
#         print(i)

printNumber = []
for i in range(secondNum+1):
    printNumber.append(i)

is_sosu = [True]*(secondNum+1)
is_sosu[0] = is_sosu[1] = False

for i in range(2,secondNum+1):
    if is_sosu[i]:
        for j in range(i*i,secondNum+1,i):
            is_sosu[j] = False

for i in printNumber:
    if is_sosu[i] == True:
        if firstNum <= printNumber[i] <= secondNum:
            print(printNumber[i])