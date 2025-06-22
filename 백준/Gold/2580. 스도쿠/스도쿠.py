import sys
input = sys.stdin.readline

board = []
blank = []
for i in range (9):
  board.append(list(map(int, input().split())))
  for j in range (9):
    if board[i][j] == 0:
      blank.append((i, j))

def check(x, y, target):
  for i in range (9):
    if board[x][i] == target: # 가로줄에 target이 이미 존재하는 경우
      return False
    
    if board[i][y] == target: # 세로줄에 target이 이미 존재하는 경우
      return False
  
  # 3*3 범위
  xr = 3 * (x//3)
  yr = 3 * (y//3)
  for i in range (xr, xr + 3):
    for j in range (yr, yr + 3):
      if board[i][j] == target:
        return False
  
  return True
  
def fill(idx):
  if idx == len(blank):
    for i in range (9):
      print(*board[i])
    exit()
  
  x, y = blank[idx]
  for i in range (1, 10):
    if check(x, y, i):
      board[x][y] = i
      fill(idx + 1)
      board[x][y] = 0

fill(0)