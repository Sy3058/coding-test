import sys
input = sys.stdin.readline

# (0, 0) -> (0, 1) -> (1, 0) -> (1, 1) 순서대로
n = int(input())
board = [list(input().strip()) for _ in range (n)]
ans = ''

def check(x, y, n):
  global ans
  if n == 1:
    return board[x][y]
  
  # 왼쪽 위
  lt = check(x, y, n//2)

  # 오른쪽 위
  rt = check(x, y + n//2, n//2)

  # 왼쪽 아래
  lb = check(x + n//2, y, n//2)

  # 오른쪽 아래
  rb = check(x + n//2, y + n//2, n//2)

  if lt == rt == lb == rb and len(lt) == 1: # 전부 같다면 '1' 혹은 '0'을 리턴 + 이전의 값이 괄호에 묶여있는 값이면 안되므로 len(lt)로 값의 길이 확인
    return lt
  
  return "(" + lt + rt + lb + rb + ")"

print(check(0, 0, n))