import sys
import math
input = sys.stdin.readline

t = int(input())
for _ in range (t):
  n = int(input())
  print('Pairs for %d: '%(n), end = '')
  pair = []
  for i in range (1, math.ceil(n/2)):
    if i != n-i:
      pair.append((i, n-i))
  
  for i in range (len(pair)):
    if i == 0: print(pair[i][0], pair[i][1], end = '')
    else: print(', %d %d'%(pair[i][0], pair[i][1]), end='')
  print()