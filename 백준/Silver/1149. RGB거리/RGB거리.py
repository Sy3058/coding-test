import sys

N = int(sys.stdin.readline()) # number of house
arr = []

for _ in range (N): # 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용
  prices = list(map(int, sys.stdin.readline().split()))
  arr.append(prices)

dp = [[0]*3 for _ in range (N)] # 비용을 저장할 dp
dp[0] = arr[0] # 첫 행의 비용은 원래의 비용과 동일

for i in range (1, N):
  # i-1행에서 현재의 색을 제외한 색들 중 최솟값과 현재 칸 비용을 더한 것을 dp[i]에 저장
  dp[i][0] = arr[i][0] + min(dp[i-1][1], dp[i-1][2])
  dp[i][1] = arr[i][1] + min(dp[i-1][0], dp[i-1][2])
  dp[i][2] = arr[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[N-1]))