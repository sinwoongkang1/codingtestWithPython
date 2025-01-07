import sys
import random

def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    pivot = random.choice(arr)
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    
    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots))

opinionCount = int(sys.stdin.readline())
if opinionCount == 0:
    print(0)
else:
    stack = [int(input()) for _ in range(opinionCount)]
    
    lower_bound = int(opinionCount * 0.15)
    upper_bound = opinionCount - lower_bound
    
    
    low_cutoff = quickselect(stack, lower_bound)
    high_cutoff = quickselect(stack, upper_bound - 1)
    
    trimmed_stack = [x for x in stack if low_cutoff < x < high_cutoff]


    SumStack = sum(trimmed_stack)
    lenStack = len(trimmed_stack)

    if lenStack == 0:  
        print(0)
    else:
        p = SumStack / lenStack
        q = SumStack // lenStack
        r = p - q
        if r >= 0.5:
            q += 1
        
        print(q)