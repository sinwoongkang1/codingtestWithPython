import heapq

count = int(input())
heap = []
for i in range(count):
    a= int(input())
    if a == 0 :
        if len(heap) == 0:
            print(0)
        else :
            print(-heapq.heappop(heap))
    else : 
        heapq.heappush(heap,-a)

# stack = []
# def findMax(data):
#     max = 0
#     for i in data:
#         if i > max :
#             max = i
#     return max
# for i in range(count):
#     a= int(input())
#     if a == 0:
#         if len(stack) ==0:
#             print(0)
#         else:
#             print(findMax(stack))
#             stack.remove(findMax(stack))
#     else:
#         stack.append(a)
        
