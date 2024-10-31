a,b = map(int,input().split())
c = int(input())
def timeMaker(time,minute,take):
    overTime = (minute+take)/60
    overMinute = (minute+take)%60
    if(overTime>0):
        time = int(time+overTime)
        minute=overMinute
    elif(minute+take<60):
        time=time
        minute = minute +take
    if(time>=24):
        time -=24
    print(time,minute)
timeMaker(a,b,c)