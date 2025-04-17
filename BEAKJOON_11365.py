import sys
flag = True

while flag:
    input_sentence = sys.stdin.readline().strip()
    stack = []
    if input_sentence == "END":
        flag = False
        break
    else:
        for i in range(len(input_sentence)-1,-1,-1):
            stack.append(input_sentence[i])
        print(*stack,sep="")