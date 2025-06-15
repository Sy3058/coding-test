import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range (n)]

dp = [[0] * n for _ in range (n)]

for i in range (n):
  for j in range (n):
    if j == 0:
      dp[i][j] = board[i][j]
    else:
      dp[i][j] = dp[i][j-1] + board[i][j]

for _ in range (m):
  x1, y1, x2, y2 = map(int, input().split())

  ans = 0
  for i in range (x1 - 1, x2):
    if y1 == 1:
      ans += dp[i][y2 - 1]
    else:
      ans += dp[i][y2 - 1] - dp[i][y1 - 2]

  print(ans)