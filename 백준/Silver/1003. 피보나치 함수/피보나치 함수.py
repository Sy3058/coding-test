import sys

T = int(sys.stdin.readline()) # 테스트 케이스의 개수

# Dynamic Programming
dp = [(0, 0)] * 41 # 모든 테스트 케이스의 경우
dp[0] = (1, 0) # 피보나치 수열이 0일 때
dp[1] = (0, 1) # 피보나치 수열이 1일 때

for i in range(2, 41):
  dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]) # dp[i]에서 0이 호출된 횟수는 dp[i-1]에서 0이 호출된 횟수 + dp[i-2]에서 0이 호출된 횟수 (1도 동일)

for _ in range(T):
  N = int(sys.stdin.readline())
  print(dp[N][0], dp[N][1])
