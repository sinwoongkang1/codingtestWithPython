a = input()
b = input()
c = input()

answer = 0

if a.isdigit():
    answer = int(a) + 3
elif b.isdigit():
    answer = int(b) + 2
elif c.isdigit():
    answer = int(c) + 1

if answer % 3 == 0 :
    if answer % 5 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")
else:
    if answer % 5 == 0 :
        print("Buzz")
    else:
        print(answer)