import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range (n)]
visited = [[False]*m for _ in range (n)] # 방문된 적 있는지 확인

directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
ep = set()

for i in range (n):
  for j in range (m):
    if box[i][j] == 1:
      ep.add((i,j))

def bfs(ep):
  nv = deque(ep)
  ep = set()

  while nv:
    x, y = nv.popleft()
    visited[x][y] = True

    for dx, dy in directions:
      nx, ny = x+dx, y+dy

      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
        if box[nx][ny] == 1: # 처음부터 토마토가 익은 상태였던 경우
          nv.append((nx, ny))
        elif box[nx][ny] == 0: # 익은 토마토 옆의 토마토 (익을 토마토)
          ep.add((nx, ny))
          box[nx][ny] = 1
          visited[nx][ny] = True
        else:
          visited[nx][ny] = True
  return ep

day = 0
while ep:
  ep = bfs(ep)
  if ep: # 새롭게 익은 토마토가 있다면 날짜 추가
    day += 1

flag = True # 익지 않은 토마토 확인

for i in range (n):
  for j in range (m):
    if box[i][j] == 0:
      flag = False
      break

if flag:
  print(day)
else:
  print(-1)