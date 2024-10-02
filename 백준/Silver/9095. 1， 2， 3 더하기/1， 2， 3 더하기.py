import sys

T = int(sys.stdin.readline().strip())

dp = [0] * 11
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range (3, len(dp)):
  dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for _ in range (T):
  test = int(sys.stdin.readline().strip())
  print(dp[test])