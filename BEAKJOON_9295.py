import sys

test_case = int(sys.stdin.readline().strip())

for case in range(test_case):
    first_number,second_number = map(int,sys.stdin.readline().strip().split())
    sum = first_number+second_number
    text = f"Case {case+1}: {sum}"
    print(text)
