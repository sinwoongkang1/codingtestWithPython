testCase = int(input())

def makeScore(data):
    sum = 0
    for i in range(1):
        huddle =      int(    9.23076  * (( 26.7      - data[i]    )**1.835))
        highRun =     int(    1.84523  * (( data[i+1] - 75         )**1.348))
        throw =       int(    56.0211  *  ((data[i+2] - 1.5        )**1.05))
        run_200 =     int(    4.99087  *((  42.5      - data[i+3]  )**1.81))
        longRun =     int(    0.188807 *((  data[i+4] - 210        )**1.41))
        throw_chang = int(    15.9803  *((  data[i+5] - 3.8        )**1.04))
        run_800 =     int(    0.11193  *((  254       - data[i+6]  )**1.88))
        sum = huddle + highRun + throw + run_200 + longRun + throw_chang + run_800
    return sum

for _ in range(testCase):
    scoreBoard = list(map(int,input().split()))
    print(makeScore(scoreBoard))