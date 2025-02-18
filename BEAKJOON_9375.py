import sys
test_case = int(sys.stdin.readline().strip())
for _ in range(test_case):
    number_of_cloth = int(sys.stdin.readline().strip())
    map = {}
    for _ in range(number_of_cloth):
        item, cloth = sys.stdin.readline().strip().split()
        if map.get(cloth) is None:
            map[cloth] = [item]
        elif cloth in map:
            map[cloth].append(item)
    count = 1
    for i in map:
        count *= (len(map[i]) + 1 )
    print(count-1)