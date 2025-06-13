import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * n
cross = []
for i in range (n):
  a, b = map(int, input().split())
  cross.append((a, b))
  dp[i] = 1
cross.sort() # 첫번째 값 기준으로 정렬

# 총 전깃줄 개수 - 교차하지 않는 전깃줄의 최대 개수 (최장 증가하는 부분 수열의 길이와 동일)
for i in range (n):
  for j in range (0, i):
    if cross[i][1] > cross[j][1]: # 교차하지 않음
      dp[i] = max(dp[j] + 1, dp[i])

print(n - max(dp))