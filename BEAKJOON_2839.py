kgramsOfSugar = int(input())

for i in range(kgramsOfSugar//3 + 1):
    for j in range(kgramsOfSugar//5 +1):
        if kgramsOfSugar == i*3 + j*5:
            print(i+j)
            break
        else:
            print(-1)
            break

