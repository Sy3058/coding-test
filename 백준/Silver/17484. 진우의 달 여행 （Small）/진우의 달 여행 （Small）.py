import sys

n, m = map(int, sys.stdin.readline().split())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range (n)]
dp = [[[float('inf')] * 3 for _ in range (m)] for _ in range (n)]

for j in range (m):
  for k in range (-1, 2): # k는 방향
    dp[0][j][k] = cost[0][j]

for i in range (1, n):
  for j in range (m):
    for k in range (-1, 2): # 현재 이동 방향
      for kp in range (-1, 2): # 이전 이동 방향
        if k != kp: # 이전과 현재의 이동 방향이 다를 때
          cp = j + kp
          if 0 <= cp < m: # 이동한 위치가 범위 안일 때
            dp[i][j][k] = min(dp[i][j][k], dp[i-1][cp][kp] + cost[i][j])

result = float('inf')
for j in range (m):
  for k in range (-1, 2):
    result = min(result, dp[n-1][j][k])

print(result)