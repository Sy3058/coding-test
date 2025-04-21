import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(input().strip()) for _ in range (r)]

directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
ans = 0
past = set(board[0][0])

def dfs(x, y, count):
  global ans
  ans = max(ans, count)

  for dx, dy in directions:
    nx, ny = x + dx, y + dy

    if 0 <= nx < r and 0 <= ny < c and not board[nx][ny] in past:
      past.add(board[nx][ny])
      dfs(nx, ny, count + 1)
      past.remove(board[nx][ny]) # 탐색 끝난 부분 제거

dfs(0, 0, 1)
print(ans)