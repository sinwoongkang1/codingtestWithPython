numberCount = int(input())
cards = []
answer = []
for i in range(numberCount):
    cards.append(i+1)

while len(cards) > 1 :
   answer.append(cards[0])
   cards.remove(cards[0])
   cards.append(cards[0])
   cards.remove(cards[0])

answer.append(cards[0])
print(*answer, sep=" ")