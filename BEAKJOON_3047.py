import sys

a_list = list(map(int,sys.stdin.readline().strip().split()))

sorted_list = sorted(a_list)
input_alphabet = sys.stdin.readline().strip()

answer = []
for i in range(len(input_alphabet)):
    if input_alphabet[i] == "A":
        answer.append(sorted_list[0])
    elif input_alphabet[i] == "B":
        answer.append(sorted_list[1])
    elif input_alphabet[i] == "C":
        answer.append(sorted_list[2])

print(*answer,sep=" ")