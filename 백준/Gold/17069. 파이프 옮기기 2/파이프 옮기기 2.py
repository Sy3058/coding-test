import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

cache = {} # (r, c, d)에서 목적지까지의 경로 수

pdd = {
  0: [(0, (0, 1)), (2, (1, 1))],
  1: [(1, (1, 0)), (2, (1, 1))],
  2: [(0, (0, 1)), (1, (1, 0)), (2, (1, 1))]
} # pipe direction dictionary

def dfs(r, c, d):
  # 끝에 도달한 경우
  if r == n - 1 and c == n - 1:
    return 1
  
  # Memoization (이미 방문된 경로라면 캐시값을 return)
  if (r, c, d) in cache:
    return cache[(r, c, d)]
  
  cnt = 0 # 방문 횟수 초기화

  for nd, (dr, dc) in pdd[d]: # next_direction
    nr, nc = r + dr, c + dc

    # board 내인지 확인
    if not (0 <= nr < n and 0 <= nc < n):
      continue

    # 장애물이 있는지 확인
    if board[nr][nc] == 1:
      continue

    # 대각선 이동시 모두 빈칸인지 확인
    if nd == 2:
      if board[r + 1][c] == 1 or board[r][c + 1] == 1:
        continue
    
    cnt += dfs(nr, nc, nd)
  
  cache[(r, c, d)] = cnt # 결과 cache에 저장
  return cnt

print(dfs(0, 1, 0))