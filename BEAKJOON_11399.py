import sys

number_of_people = int(sys.stdin.readline().strip())
people_wating_minutes = list(sys.stdin.readline().strip().split())
wating_times = []

for i in range(number_of_people):
    people = i+1
    wating_times.append([people,int(people_wating_minutes[i])])
   
new_order = sorted(wating_times, key=lambda x:x[1])

sum = 0
for i in range(len(new_order)):
    a = len(new_order) - i
    new_order[i][1] = new_order[i][1] * a
    sum += new_order[i][1]

print(sum)