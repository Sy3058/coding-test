n = int(input())

dp = [[0]*10 for _ in range (n+1)]

for i in range (1, 10): # 첫번째 경우는 0을 제외하고 모든 숫자가 하나씩 올 수 있음
  dp[1][i] = 1

for i in range (2, n+1):
  for j in range (10):
    if j == 0:
      dp[i][j] = dp[i-1][1] # i번째 0의 개수는 i-1번째에 있는 1의 개수
    elif j == 9:
      dp[i][j] = dp[i-1][8] # i번째 9 의 개수는 i-1번째에 있는 8의 개수
    else:
      dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % 1000000000)