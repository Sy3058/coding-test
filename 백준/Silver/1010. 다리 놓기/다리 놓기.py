import sys
input = sys.stdin.readline

t = int(input())
dp = [[0]*31 for _ in range (31)]
for i in range (1, 31):
  dp[1][i] = i

for i in range (2, 31):
  for j in range (i, 31):
    for k in range (1, j):
      dp[i][j] += dp[i-1][k]

for _ in range (t):
  n, m = map(int, input().split())
  print(dp[n][m])
