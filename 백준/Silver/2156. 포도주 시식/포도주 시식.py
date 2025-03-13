import sys
input = sys.stdin.readline

n = int(input())
wine = [int(input()) for _ in range (n)]
dp = [0]*n

dp[0] = wine[0]

# 1. 전전 포도주는 마시지 않고 전 포도주와 이번 포도주를 마심 (dp[i-3] + wine[i-1] + wine[i])
# 2. 전전 포도주와 이번 포도주를 마시고 전 포도주를 마시지 않음 (dp[i-2] + wine[i])
# 3. 현재 포도주를 마시지 않음 (dp[i-1])

if n > 1:
  dp[1] = wine[0] + wine[1]

if n > 2:
  dp[2] = max(wine[2] + wine[1], wine[2] + wine[0], dp[1])

for i in range (3, n):
  dp[i] = max(dp[i-1], dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i])

print(dp[n-1])