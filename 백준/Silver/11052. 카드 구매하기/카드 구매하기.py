import sys
import math
input = sys.stdin.readline

n = int(input()) # 가지려고 하는 카드의 개수
card = [0] + list(map(int, input().split()))
dp = card.copy()

for i in range (1, n+1):
  tmp = 0
  for j in range (math.ceil(i/2), i+1): # 이전의 카드들의 조합 중 가장 큰 값을 확인
    tmp = max(dp[i-j] + dp[j], tmp)
  dp[i] = tmp
  
print(dp[-1])