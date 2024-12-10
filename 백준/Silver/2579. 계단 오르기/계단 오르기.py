import sys

n = int(sys.stdin.readline()) # 계단의 개수
dp = [0] * (n+1)
scores = [0] * (n+1)
for i in range (1, n+1):
  scores[i] = int(sys.stdin.readline())

if n == 1:
  print(scores[1])

elif n == 2:
  print(scores[1]+scores[2])

else:
  dp[1] = scores[1]
  dp[2] = scores[1] + scores[2]

  for i in range (3, n+1):
    c1 = dp[i-3] + scores[i-1] + scores[i] # i-1번째 계단을 밟고 오는 경우 (i-2번째 계단은 건너 뛰어야함)
    c2 = dp[i-2] + scores[i] # i-2번째 계단을 밟고 오는 경우 (i-1번째 계단을 건너 뛰어야함)
    dp[i] = max(c1, c2)
  
  print(dp[-1])