import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
iarr = [] # input array
s = ()
for i in range (n):
  row = list(map(int, sys.stdin.readline().split()))
  iarr.append(row)
  if s: # 2 appears once in array
    continue
  else:
    for j in range (m):
      if row[j] == 2:
        s = (i, j) # start point == 2
darr = [[0]*m for _ in range (n)] # distance array (answer)
darr[s[0]][s[1]] = 0

def bfs(start):
  nv = deque() # need visited
  nv.append(start)

  directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

  while nv:
    x, y = nv.popleft()

    for dx, dy in directions: # move directions
      nx, ny = x + dx, y + dy

      if 0 <= nx < n and 0 <= ny < m and iarr[nx][ny] == 1 and darr[nx][ny] == 0: # within range, can be visited, and not visited yet
        nv.append((nx, ny))
        darr[nx][ny] = darr[x][y] + 1
  
  return darr

darr = bfs(s)

# 갈 수 있었지만 갈 수 없게된 땅 확인
for i in range (n):
  for j in range (m):
    if iarr[i][j] == 1 and darr[i][j] == 0:
      darr[i][j] = -1

for i in range (n):
  print(' '.join(map(str,darr[i])))