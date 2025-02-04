import sys

testCase = int(sys.stdin.readline().strip())

def find_number_of_peoples(floor,room):
    arr = []
    brr = []
    for i in range(1,room+1):
        arr.append(i)
    for i in range(floor):       
        for j in range(room):
            brr.append(sum(arr[:j+1]))
        arr = brr
        brr = []
    return arr[room-1]

for _ in range(testCase):
    floor = int(sys.stdin.readline().strip())
    room = int(sys.stdin.readline().strip())
    print(find_number_of_peoples(floor,room))
