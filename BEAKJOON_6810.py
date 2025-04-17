import sys

first_number = int(sys.stdin.readline().strip())
second_number = int(sys.stdin.readline().strip())
third_number = int(sys.stdin.readline().strip())

standard = str(9780921418)

sum = 0

for i in range(len(standard)):
    if i % 2 == 0:
         sum += int(standard[i]) * 1
    else:
        sum += int(standard[i]) * 3

print_num =  sum + first_number +second_number*3 + third_number

print("The 1-3-sum is",print_num)

