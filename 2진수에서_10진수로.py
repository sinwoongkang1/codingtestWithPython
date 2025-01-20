N = str(input("2진수를 입력하세요: "))
total = 0
for char in N:
    if char not in '01':
        print("유효하지 않은 2진수.")
        break
else:  
    for i in range(len(N)):
        total += int(N[i]) * (2 ** ((len(N) - 1) - i))

    print(f"10진수: {total}")