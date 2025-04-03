import sys
input = sys.stdin.readline

n = int(input())
o = [0] + [int(input()) for _ in range (n)] # order

dp = [1] * (n+1)

# find the longest increasing sequence
for i in range (1, n+1):
  for j in range (1, i):
    if o[j] < o[i]: # if number has increased
      dp[i] = max(dp[i], dp[j] + 1)

print(n-max(dp))
