import sys
input = sys.stdin.readline
from collections import deque

def sol():
  m, n, h = map(int, input().split())
  board = []
  ripe_tomato = deque()

  # 입력
  for hei in range(h):
    floor = []
    for row in range(n):
      line = list(map(int, input().split()))
      floor.append(line)
      for col in range(m):
        if line[col] == 1:
          ripe_tomato.append((hei, row, col, 0)) # 위치, 익은 날짜
    board.append(floor)

  # 이동 방향은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
  # 순서대로 dh, dr, dc
  deltas = ((0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0))

  while ripe_tomato:
    hei, row, col, date = ripe_tomato.popleft()

    for dh, dr, dc in deltas:
      nh, nr, nc = hei + dh, row + dr, col + dc

      if 0 <= nh < h and 0 <= nr < n and 0 <= nc < m and board[nh][nr][nc] == 0:
        ripe_tomato.append((nh, nr, nc, date + 1)) # 현재 날짜 다음날 익음
        board[nh][nr][nc] = 1
  
  for hei in range (h):
    for row in range (n):
      for col in range (m):
        if board[hei][row][col] == 0:
          print(-1)
          return
        
  print(date) # 마지막으로 익은 날짜

sol()