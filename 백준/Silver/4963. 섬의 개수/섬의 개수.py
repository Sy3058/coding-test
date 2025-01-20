import sys
from collections import deque
input = sys.stdin.readline

def bfs(s):
  nv = deque([s])
  directions = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)] # 대각선 포함 8방향

  while nv:
    x, y = nv.popleft()
    for dx, dy in directions:
      nx, ny = x + dx, y + dy
      if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx] and m[ny][nx] == 1: # 범위 내, 방문된 적 없는 땅
        nv.append((nx, ny))
        visited[ny][nx] = True

w, h = map(int, input().split())

while w != 0 and h != 0:
  m = [] # 지도
  for _ in range (h):
    arr = list(map(int, input().split()))
    m.append(arr)
  
  visited = [[False] * w for _ in range (h)]
  cnt = 0 # 땅의 개수

  for i in range (w):
    for j in range (h):
      if m[j][i] == 1 and not visited[j][i]:
        s = (i, j)
        bfs(s)
        cnt += 1
  
  print(cnt)
  w, h = map(int, input().split())