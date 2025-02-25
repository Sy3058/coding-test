import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range (n)]
com = list(map(int, input().split()))
dice = [0] * 7

md = {1:(0, 1), 2:(0, -1), 3:(-1, 0), 4:(1, 0)} # map direction
dd = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6} # dice direction

def dm(c):
  if c == 1:
    dd[1], dd[6], dd[3], dd[4] = dd[4], dd[3], dd[1], dd[6]
  elif c == 2:
    dd[1], dd[6], dd[3], dd[4] = dd[3], dd[4], dd[6], dd[1]
  elif c == 3:
    dd[1], dd[6], dd[2], dd[5] = dd[5], dd[2], dd[1], dd[6]
  else:
    dd[1], dd[6], dd[2], dd[5] = dd[2], dd[5], dd[6], dd[1]

for c in com:
  dx, dy = md[c]
  nx, ny = x+dx, y+dy
  if nx < 0 or ny < 0 or nx >= n or ny >= m:
    continue
  x, y = nx, ny
  dm(c)
  if board[x][y] == 0:
    board[x][y] = dice[dd[6]]
  
  else:
    board[x][y], dice[dd[6]] = 0, board[x][y]

  print(dice[dd[1]])