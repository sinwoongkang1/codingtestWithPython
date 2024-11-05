from collections import deque

cardCount = int(input())
queue = deque([])

for i in range(1,cardCount+1):
    queue.append(i)
while len(queue)>1 :
    del queue[0]
    queue.append(queue[0])
    del queue[0]
print(queue[0])