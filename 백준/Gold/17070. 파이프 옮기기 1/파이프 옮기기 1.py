import sys
input = sys.stdin.readline

"""
r은 행의 번호, c는 열의 번호
가능한 이동 범위
가로: (0, 1), (1, 1)
세로: (1, 0), (1, 1)
대각선: (0, 1), (1, 0), (1, 1)
=> (1, 1)인 경우 (0, 1), (1, 0), (1, 1) 모두 빈 칸이어야 함
Q1. 현재 파이프의 방향 확인?
A1. 파이프의 이동 방향 앞에 방향을 붙여서 저장 // (0, (1, 0))과 같이 저장 가능
Q2. 시간 초과 해결?
A2. cache 딕셔너리를 이용해서 {(r, c, d) : 방문횟수}를 저장
확인해야할 조건이 많은 경우 if ~ continue 구문을 이용해서 정리 가능
"""

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