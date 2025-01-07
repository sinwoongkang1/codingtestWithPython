from collections import deque

N, K = map(int,input().split())
queue = deque()
for i in range(1,N+1):
    queue.append(i)
answer = []

while len(queue) != 0:
    a = len(queue)
    b = K % a
    c = b - 1
    answer.append(queue[c])
    del queue[c]
    for _ in range(c):
        queue.append(queue[0])
        queue.popleft()


formatted_answer = f"<{', '.join(map(str, answer))}>"
print(formatted_answer)