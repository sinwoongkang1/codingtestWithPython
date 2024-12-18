# numCount, numSum = map(int,input().split())
# array = list(map(int,input().split()))
# count = 0
# for i in range(len(array)):
#     sum = 0
#     for j in range(i,len(array)):
#         sum += array[j]
#         if sum == numSum:
#             count += 1
# print(count)

numCount, numSum = map(int, input().split())
array = list(map(int, input().split()))

count = 0
current_sum = 0
sum_count = {0: 1}

for num in array:
    current_sum += num 
    if current_sum - numSum in sum_count:
        count += sum_count[current_sum - numSum] 
    if current_sum in sum_count:
        sum_count[current_sum] += 1  
    else:
        sum_count[current_sum] = 1 

print(count)

# count = 0
# left = 0
# right = 1

# while left == right:
#     target = sum(array[left:right])
#     if target < numSum:
#         right += 1
#     if target == numSum:
#         count += 1
#         right +=1
#     else :
#         left += 1

# print(count)
        