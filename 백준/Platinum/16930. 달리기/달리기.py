import sys
input = sys.stdin.readline
from collections import deque

# 체육관의 크기, 이동할 수 있는 칸의 최대 개수
n, m, k = map(int, input().split())
board = [list(input().strip()) for _ in range (n)]
x1, y1, x2, y2 = map(int, input().split())
x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1 # 1, 1부터 시작하므로
deltas = ((1, 0), (0, 1), (-1, 0), (0, -1))
dist = [[-1] * m for _ in range (n)] # -1이면 미방문

def solve():
  if x1 == x2 and y1 == y2:
    print(0)
    return

  nv = deque([(x1, y1)])
  dist[x1][y1] = 0

  while nv:
    x, y = nv.popleft()

    for dx, dy in deltas:
      # 각 방향으로 k칸까지 탐색
      for re in range (1, k+1):
        nx, ny = x + dx * re, y + dy * re

        # 범위를 벗어나거나 벽을 만나면 탐색 중단
        if not (0 <= nx < n and 0 <= ny < m and board[nx][ny] == '.'): break

        # 더 빨리 도착한 적 있는 경우 더 진행할 필요 없음
        if dist[nx][ny] != -1 and dist[nx][ny] <= dist[x][y]: break

        # 이미 방문한 칸을 만나면 그 방향 탐색 중단 (이미 앞에서 탐색했으므로)
        if dist[nx][ny] != -1: continue

        dist[nx][ny] = dist[x][y] + 1 # 현재 있는 칸에서 다음 칸 방문이므로 시간 + 1
        if nx == x2 and ny == y2:
          print(dist[nx][ny])
          return
        nv.append((nx, ny))
  
  # 큐가 비었는데도 도달하지 못했다면 갈 수 없는 곳
  print(-1)

solve()