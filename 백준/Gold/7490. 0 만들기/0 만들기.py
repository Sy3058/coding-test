import sys
import itertools
input = sys.stdin.readline

t = int(input()) # test case
co = ('', '+', '-') # operators that can be selected (in ASCII code order)

for _ in range (t):
  n = int(input())
  arr = []
  x = 1
  for i in range (2*n - 1):
    if i % 2 == 0:
      arr.append(str(x))
      x += 1
    else:
      arr.append('')
  
  ei = [i for i in range (1, 2*n - 1, 2)] # index where operator should be in
  coo = list(itertools.product(co, repeat=n-1)) # combination of operators
  
  for c in coo:
    for i, op in zip(ei, c): # change operator
      arr[i] = op
      
    if eval(''.join(arr)) == 0:
      for j in range (1, 2*n - 1, 2):
        if arr[j] == '': arr[j] = ' '

      print(''.join(arr))
  
  print()