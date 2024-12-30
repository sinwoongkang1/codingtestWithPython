numberOfPeoples= int(input())
peoles = []
for _ in range(numberOfPeoples):
    age,name = map(str,input().split())
    peoles.append([int(age),name])

for i in sorted(peoles,key=lambda x : x[0]):
    print(i[0],i[1])