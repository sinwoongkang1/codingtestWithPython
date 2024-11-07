chattingCount = int(input())
chatRoom = set() 
countGomGom = 0

for i in range(chattingCount):
    chat = input()
    
    if chat == "ENTER":
        chatRoom.clear()  
    else:
        if chat not in chatRoom:
            chatRoom.add(chat)
            countGomGom += 1
print(countGomGom)