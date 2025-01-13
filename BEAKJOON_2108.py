import sys

numberCount = int(sys.stdin.readline())
stack = []
for _ in range(numberCount):
    stack.append(int(sys.stdin.readline()))

def average(stack):
    return round(sum(stack) / len(stack))

def center(stack):
    stack.sort()
    return stack[(len(stack)//2)]

def moreAppearance(stack):
    map = {}
    for i in stack:
        if i not in map:
            map[i] = 1
        else:
            map[i] += 1
    sorted_map = dict(sorted(map.items(), key=lambda item: item[1]))
    max = 0
    answer = []
    for i in sorted_map:
        sorted_map[i] >= max
        max = sorted_map[i]
    for i in sorted_map:
        if max == sorted_map[i]:
            answer.append(i)
    if len(answer) == 1:
        return answer[0]
    else:
        return answer[1]

def range(stack):
    stack.sort()
    return stack[-1] - stack[0]

print(average(stack))
print(center(stack))
print(moreAppearance(stack))
print(range(stack))
