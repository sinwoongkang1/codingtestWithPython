x1,y1 = map(int,(input().split()))
x2,y2 = map(int,(input().split()))
x3,y3 = map(int,(input().split()))

x_arr = [x1,x2,x3]
y_arr = [y1,y2,y3]

for i in range(len(x_arr)):
    if x_arr.count(x_arr[i]) == 1 :
        x4 = x_arr[i]
    if y_arr.count(y_arr[i]) == 1 :
        y4 = y_arr[i]

print(x4,y4)