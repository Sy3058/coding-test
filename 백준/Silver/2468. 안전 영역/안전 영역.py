import sys
from collections import deque

n = int(sys.stdin.readline())
area = [list(map(int, sys.stdin.readline().split())) for _ in range (n)]

maxh = max(max(row) for row in area) # 높이 최댓값

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(x, y, h):
  nv = deque([(x, y)])
  visited[x][y] = True

  while nv:
    cx, cy = nv.popleft() # 현재 x, y
    for dx, dy in directions:
      nx, ny = cx + dx, cy + dy
      if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and area[nx][ny] > h: # 방문된 적 없고 물에 잠기지 않는 경우 (범위 내) 
        nv.append((nx, ny))
        visited[nx][ny] = True

ans = 0
for h in range (maxh+1):
  visited = [[False] * n for _ in range (n)]
  cnt = 0
  for i in range (n):
    for j in range (n):
      if area[i][j] > h and not visited[i][j]: # 방문된 적 없고 물에 잠기지 않는 경우
        bfs(i, j, h)
        cnt += 1
  
  ans = max(ans, cnt)

print(ans)