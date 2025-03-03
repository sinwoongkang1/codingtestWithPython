import sys

flag = True

while flag:
    user_input = str(sys.stdin.readline().strip())
    if user_input == "#":
        flag = False
        break
    count = 0
    for i in range(len(user_input)):
        if user_input[i] == "a" or user_input[i] == "e" or user_input[i] == "i" or user_input[i] == "o" or user_input[i] == "u":
            count += 1
        if user_input[i] == "A" or user_input[i] == "E" or user_input[i] == "I" or user_input[i] == "O" or user_input[i] == "U":
            count += 1
    print(count)