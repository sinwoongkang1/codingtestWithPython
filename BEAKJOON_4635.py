flag = True
while flag:
    data = int(input())
    if data == -1:
        flag = False
    else:
        mp=[]
        tt=[]
        for i in range(data):
            milePerHour,totalTime = map(int,input().split())
            mp.append(milePerHour)
            if len(tt) == 0:
                tt.append(totalTime)
            elif len(tt) > 0:
                tt.append(totalTime-sum(tt))
        total = 0
        for i in range(data):
            total += mp[i] * tt[i]
        print(total,"miles")
