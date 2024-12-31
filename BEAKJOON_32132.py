N = int(input())
S = str(input())
flag = True

while flag :
    for i in range(len(S)-2):
        if S[i] == "P":
            if S[i+1] == "S":
                if S[i+2] == "4":
                    S = S[:i+2]+ S[i+3:]
                elif S[i+2] == "5": 
                    S = S[:i+2]+ S[i+3:]
    if "PS4" not in S :
        if "PS5" not in S:
            break
print(S)