pocketmonCount, question = map(int,input().split())
pocketmonStack = {}
questionStack = []
for i in range(pocketmonCount):
    pocketMonname = str(input())
    pocketmonStack[i+1] = pocketMonname
    pocketmonStack[pocketMonname] = i+1
for _ in range(question):
    questionStack.append(input())
for i in questionStack:
    if i.isdigit():
        print(pocketmonStack[int(i)])
    else:
        print(pocketmonStack[i])