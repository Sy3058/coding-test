import sys

N = int(sys.stdin.readline())

# 최대 N만큼 dp 생성
dp = [0] * 1000001

for i in range (2, N+1):
  # 1을 뺀 경우
  dp[i] = dp[i-1] + 1

  # 2로 나누어 떨어지는 경우 (dp[i]는 이미 dp[i-1]에 1을 더한 값)
  if i%2 == 0:
    dp[i] = min(dp[i], dp[i//2] + 1)

  # 3으로 나누어 떨어지는 경우 (dp[i]는 이미 dp[i]와 dp[i//2] + 1 중 작은 값)
  if i%3 == 0:
    dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[N])