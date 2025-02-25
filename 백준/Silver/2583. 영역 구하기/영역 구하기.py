import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())
board = [[True]*n for _ in range (m)]
for _ in range (k):
  x1, y1, x2, y2 = map(int, input().split())
  for i in range (x1, x2):
    for j in range (y1, y2):
      board[j][i] = False
cnt = 0
size = []

def dfs(s):
  nv = [s]
  directions = [(0,1), (0,-1), (1,0), (-1,0)]
  ss = 1

  while nv:
    x, y = nv.pop()
    for dx, dy in directions:
      nx, ny = x+dx, y+dy
      if 0 <= nx < n and 0 <= ny < m and board[ny][nx]:
        nv.append((nx, ny))
        ss += 1
        board[ny][nx] = False
  
  size.append(ss)

for i in range (n):
  for j in range (m):
    if board[j][i]:
      board[j][i] = False
      dfs((i, j))
      cnt += 1

size.sort()

print(cnt)
print(*size)