import sys

test_case = int(input())
numbers= []
sentence = []
for i in range(test_case):
    numbers.append(int(i)+1)
    input_line = str(input())
    sentence.append(input_line)

for i in range(test_case):
    print(str(numbers[i])+".",sentence[i])
