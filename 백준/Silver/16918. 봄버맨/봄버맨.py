import sys
input = sys.stdin.readline

r, c, n = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

if n <= 1: # initial state
  for row in board:
    print(''.join(row))

elif n % 2 == 0: # board is full of bomb
  for _ in range (r):
    print('O' * c)

else:
  # state after first explosion
  ep1 = [['O'] * c for _ in range (r)]
  for i in range (r):
    for j in range (c):
      if board[i][j] == 'O': # bomb refer to initial state
        ep1[i][j] = '.' # bomb explodes

        for di, dj in directions:
          ni, nj = i + di, j + dj
          if 0 <= ni < r and 0 <= nj < c:
            ep1[ni][nj] = '.' # nearby areas explode
  
  # state after second explosion
  ep2 = [['O'] * c for _ in range (r)]
  for i in range (r):
    for j in range (c):
      if ep1[i][j] == 'O': # bomb refer to ep1
        ep2[i][j] = '.'

        for di, dj in directions:
          ni, nj = i + di, j + dj
          if 0 <= ni < r and 0 <= nj < c:
            ep2[ni][nj] = '.'
  
  if n % 4 == 3:
    for row in ep1:
      print(''.join(row))
  
  elif n % 4 == 1:
    for row in ep2:
      print(''.join(row))