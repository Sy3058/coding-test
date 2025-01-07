import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range (t):
  n, m = map(int, input().split())
  imp = list(map(int, input().split()))
  doc = deque(list(enumerate(imp)))
  flag = False
  
  imp.sort(reverse=True)
  for i in range (n):
    for j in range (len(doc)):
      if doc[j][1] == imp[i]:
        if doc[j][0] == m:
          ans = i + 1
          flag = True
          break
        doc.rotate(-j)
        doc.popleft()
        break
    if flag:
      break
  
  print(ans)