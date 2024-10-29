import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split()) # 위치
arr = []

# 미로
for _ in range (N):
  row = list(map(int, sys.stdin.readline().strip()))
  arr.append(row)

def bfs(x, y):
  nv = deque() # 방문해야하는 위치
  nv.append((x, y))
  directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

  while nv:
    x, y = nv.popleft()

    for dx, dy in directions:
      nx, ny = x + dx, y + dy

      if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
        nv.append((nx, ny))
        arr[nx][ny] = arr[x][y] + 1 # 이전 위치에서 한 칸 이동했으므로 이동거리 1 증가
  
  return arr[N-1][M-1]

print(bfs(0, 0))