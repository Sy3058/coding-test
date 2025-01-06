import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

dp = [1 for i in range (n)] # 자기 자신을 포함하므로 모든 부분 수열은 1 이상

for i in range (1, n):
  for j in range (0, i):
    if A[j] < A[i]: # A[i] 이전에 A[i]보다 작은 수가 있는 경우
      dp[i] = max(dp[i], dp[j] + 1) # dp[j]에 A[i]를 추가한 수와 dp[i] 중 더 큰 것을 저장

print(max(dp))