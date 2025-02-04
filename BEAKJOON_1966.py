import sys
testCase = int(sys.stdin.readline().strip())

def get_max_first_index(arr):
    first_values = [subarr[0] for subarr in arr]
    max_value = max(first_values)
    return max_value
    
def orderPrint(data,target):
    arr = [[0, 0] for _ in range(len(data))]
    for i in range(len(data)):
        if i == target:
            arr[i][0] = data[i]
            arr[i][1] = 1
        else:
            arr[i][0] = data[i]
            arr[i][1] = 0
    count = 0
    while True:
        max = get_max_first_index(arr)
        if arr[0][0] != max:
            arr.append(arr[0])
            del arr[0]
        else:
            count += 1
            if arr[0][1] == 1:
                print(count)
                break
            else:
                del arr[0]
 
for _ in range(testCase):                       
    documentsCount, targetDocument = map(int,sys.stdin.readline().strip().split())
    documents = list(map(int,sys.stdin.readline().split()))
    orderPrint(documents,targetDocument)
