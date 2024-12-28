def solution (arr):
    answer = []
    for i in range(1,len(arr)):
        if arr[i-1] not in answer:
            answer.append(arr[i-1])
        if arr[i-1] != arr[i]:
            answer.append(arr[i])
    return print(answer)

stack = [4, 4, 4, 3, 3]
solution(stack)