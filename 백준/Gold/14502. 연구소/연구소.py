from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
empty = []
virus = set()
deltas = ((1, 0), (0, 1), (-1, 0), (0, -1))
min_virus = float('inf')
wall_cnt = 0

for i in range (n):
  b = list(map(int, input().split()))
  board.append(b)
  for j in range (m):
    if b[j] == 0:
      empty.append((i, j))
    elif b[j] == 2:
      virus.add((i, j))
    else:
      wall_cnt += 1

def make_combination(empty):
  # 빈 곳 중 3곳을 골라 벽 설치 (최대 41664)
  l = len(empty)
  combination = []
  for i in range (l):
    for j in range (i+1, l):
      for k in range (j+1, l):
        combination.append((i, j, k))
  return combination

def install_wall(comb):
  # comb = (i, j, k)
  i, j, k = comb
  xi, yi = empty[i]
  xj, yj = empty[j]
  xk, yk = empty[k]
  board[xi][yi] = 1
  board[xj][yj] = 1
  board[xk][yk] = 1

def demolish_wall(comb):
  i, j, k = comb
  xi, yi = empty[i]
  xj, yj = empty[j]
  xk, yk = empty[k]
  board[xi][yi] = 0
  board[xj][yj] = 0
  board[xk][yk] = 0

def count_virus(virus):
  visited = [[False] * m for _ in range (n)]
  cnt = 0

  def dfs(x, y, cnt):
    nv = deque([(x, y)])

    while nv:
      if cnt > min_virus:
        # 바이러스가 최소값보다 더 퍼졌다면 더 검사할 필요 없음
        return float('inf'), False
      
      cx, cy = nv.popleft()

      for dx, dy in deltas:
        # 4 방향 확인
        nx, ny = cx + dx, cy + dy

        # 범위 안이고 방문한 적 없는 경우
        if (0 <= nx < n and 0 <= ny < m and not visited[nx][ny]):
          if board[nx][ny] == 1: # 1일때는 방문처리만
            visited[nx][ny] = True
          
          elif board[nx][ny] == 0: # 비어있을 때만 퍼지기 가능
            visited[nx][ny] = True
            cnt += 1
            nv.append((nx, ny))

    return cnt, True # 중단 없이 완료된 경우

  for x, y in virus:
    visited[x][y] = True
    cnt += 1
    cnt, success = dfs(x, y, cnt)
    if not success: # 가지치기
      break
  
  return cnt

combination = make_combination(empty) # empty 기준 인덱스만 들어가 있음
for comb in combination: # comb = (i, j, k)
  install_wall(comb)
  min_virus = min(min_virus, count_virus(virus))
  demolish_wall(comb)

print(n*m - min_virus - wall_cnt - 3) # 벽을 3개 설치했을 때 결과이므로