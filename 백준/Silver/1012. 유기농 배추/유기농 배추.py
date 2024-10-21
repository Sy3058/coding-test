import sys
from collections import deque

def bfs(field, visited, sy, sx, N, M):
  # 이동 가능한 방향 (상, 하, 좌, 우)
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  nv = deque([(sy, sx)]) # 방문이 필요한 좌표를 저장
  visited[sy][sx] = True # 방문된 곳은 True로 변경

  while nv: # 방문이 필요한 곳이 있다면
    y, x = nv.popleft()

    for dy, dx in directions:
      ny, nx = y + dy, x + dx # 현재 좌표에 상하좌우 이동시킨 값

      if 0 <= ny < N and 0 <= nx < M and field[ny][nx] == 1 and not visited[ny][nx]: # 유효한 범위 내에 있고 배추가 있으며 방문되지 않은 경우
        visited[ny][nx] = True
        nv.append((ny, nx))

T = int(sys.stdin.readline()) # test case
for _ in range (T):
  M, N, K = map(int, sys.stdin.readline().split()) # 배추밭의 가로길이, 세로길이, 심어진 위치 개수
  field = [[0]*M for _ in range (N)]
  visited = [[False]*M for _ in range (N)]

  for _ in range (K):
    X, Y = map(int, sys.stdin.readline().split())
    field[Y][X] = 1 # 배추가 심어진 위치 표시
  
  cnt = 0 # 필요한 배추흰지렁이 수

  for i in range (N):
    for j in range (M):
      if field[i][j] == 1 and not visited[i][j]: # 배추가 있으나 방문되지 않은 경우
        bfs(field, visited, i, j, N, M)
        cnt += 1
  
  print(cnt)