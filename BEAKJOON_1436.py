import sys

movieSeries = int(sys.stdin.readline().strip())
count = 0
number_Of_World_Ending = 666

while True:
    if '666' in str(number_Of_World_Ending):
      count += 1
    if count == movieSeries:
       break
    number_Of_World_Ending += 1

print(number_Of_World_Ending)
