N = int(input("10진수를 입력하세요: "))

if N < 0:
    print("음수는 입력할 수 없음.")
else:
    stack = []

    while N > 0:
        stack.append(N % 2)
        N //= 2

    if len(stack) < 8:
        zero = [0] * (8 - len(stack))
        stack.extend(zero)

    print(*stack[::-1], sep="")