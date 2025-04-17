import sys

user_input = sys.stdin.readline().strip()
word_filter = ["a","e","i","o","u"]
count = 0

for i in range(len(user_input)):
    if user_input[i] in word_filter:
        count += 1

print(count)


