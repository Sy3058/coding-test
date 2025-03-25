import sys
input = sys.stdin.readline

def determine(board):
  Xs = board.count('X')
  Os = board.count('O')
  rest = 9 - Xs - Os

  # need at least 3 Xs or Os to make bingo (need bingo to be finished if the board is not full)
  if Xs < 3 and Os < 3:
    return 'invalid'

  # X starts first and O comes next
  if Xs - Os not in (0, 1):
    return 'invalid'
  
  xf, of = bingo(board)
  if xf and of: # only one of x or o can be bingo
    return 'invalid'
  
  # board should be full if there is no bingo
  if not xf and not of and board.count('.') != 0:
    return 'invalid'
  
  # if one is finished, another can't be added
  if xf and Os != Xs - 1:
    return 'invalid'
  
  if of and Xs != Os:
    return 'invalid'

  return 'valid'

def bingo(board):
  xf = False # flag for x
  of = False # flag for o
  # diagonal
  if board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
    if board[4] == 'X':
      xf = True
    elif board[4] == 'O':
      of = True
  
  # horizontal
  for i in range (0, 9, 3):
    if board[i] == board[i+1] == board[i+2]:
      if board[i+1] == 'X':
        xf = True
      elif board[i+1] == 'O':
        of = True
  
  # vertical
  for i in range (3):
    if board[i] == board[i+3] == board[i+6]:
      if board[i+3] == 'X':
        xf = True
      elif board[i+3] == 'O':
        of = True
  
  return xf, of
  

board = input().strip()

while board != 'end':
  board = list(board)
  print(determine(board))

  board = input().strip()