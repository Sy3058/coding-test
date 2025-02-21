import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [arr[i] for i in range (n)]

for i in range (1, n):
  dp[i] = max(dp[i-1]+arr[i], dp[i])

print(max(dp))