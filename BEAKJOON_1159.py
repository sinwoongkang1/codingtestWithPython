playerCount = int(input())
map = {}
stack = []
for i in range(playerCount):
    playerName = str(input())
    if playerName[0] not in map:
        map[playerName[0]] = 1
    elif playerName[0] in map:
        updateKey = map.get(playerName[0]) +1
        map[playerName[0]] = updateKey
for i in map.keys():
    if map[i] >= 5:
        stack.append(i)
stack.sort()
if len(stack) > 0:
    print(*stack,sep="")
else :
    print("PREDAJA")