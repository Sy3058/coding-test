import sys

t = int(sys.stdin.readline()) # test case

dp = [0 for _ in range (101)] # max n == 100

P = [0, 1, 1, 1, 2, 2]

i = 1
while len(dp) != i:
  if i <= 5:
    dp[i] = P[i]
    i += 1
  else:
    dp[i] = dp[i-1] + dp[i-5]
    i += 1

for _ in range (t):
  n = int(sys.stdin.readline())
  print(dp[n])
