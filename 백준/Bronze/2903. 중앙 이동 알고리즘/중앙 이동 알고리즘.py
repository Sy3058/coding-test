import sys

n = int(sys.stdin.readline())

dp = [0] * 16
dp[0] = 4
for i in range (1, 16):
  dp[i] = int(((dp[i-1] ** 0.5)*2 - 1)**2)

print(dp[n])