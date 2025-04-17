import sys

swap = {'i': 'e', 'e': 'i', 'I': 'E', 'E': 'I'}

for line in sys.stdin:
    line = line.strip()
    print(''.join(swap.get(c, c) for c in line))