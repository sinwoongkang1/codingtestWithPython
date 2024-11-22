import itertools

stack = []
for _ in range(9):
    a = int(input())
    stack.append(a)
난쟁이들 = itertools.combinations(stack, 7)
for 조합 in 난쟁이들:
    조합_sum = sum(조합)
    if 조합_sum == 100:
        난쟁이조합 = 조합
answer = []
for i in 난쟁이조합:
    answer.append(i)
answer.sort()

for i in answer:
    print(i)