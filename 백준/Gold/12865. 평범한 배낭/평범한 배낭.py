import sys
input = sys.stdin.readline

n, k = map(int, input().split())

obj = [[0, 0]]
dp = [[0] * (k+1) for _ in range (n+1)]

for i in range (n):
  obj.append(list(map(int, input().split())))

for i in range (1, n+1):
  for j in range (1, k+1):
    w, v = obj[i]

    if j < w: # 허용 무게보다 더 무거우면 넣을 수 없음
      dp[i][j] = dp[i-1][j]
    
    else: # 넣었을 때와 넣지 않았을 때 중 더 가치가 높은 것
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[n][k])