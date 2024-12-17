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
sum_count = {0: 1}  # 초기 상태: 부분합이 0인 경우가 1개

for num in array:
    current_sum += num  # 현재까지의 누적 합
    if current_sum - numSum in sum_count:
        count += sum_count[current_sum - numSum]  # 목표 합을 만들 수 있는 경우의 수 추가
    if current_sum in sum_count:
        sum_count[current_sum] += 1  # 현재 누적 합을 해시맵에 추가
    else:
        sum_count[current_sum] = 1  # 새로운 누적 합을 해시맵에 추가

print(count)