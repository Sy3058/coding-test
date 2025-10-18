import sys
input = sys.stdin.readline

n, m, r = map(int, input().split()) # 지역 개수, 수색 범위, 길의 개수
items = [0] + list(map(int, input().split()))
dp = [[float('inf') for _ in range (n + 1)] for __ in range (n+1)]
for _ in range (r):
  a, b, l = map(int, input().split())
  # 연결된 지역과 거리를 함께 저장
  dp[a][b] = min(l, dp[a][b])
  dp[b][a] = min(l, dp[b][a])
for i in range (n + 1): # 자기 자신으로 가는 최소값은 항상 0
  dp[i][i] = 0

for k in range (1, n+1): # 경유지
  for i in range (1, n+1): # 출발지
    for j in range (1, n+1): # 도착지
      dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]) # i 지역에서 j 지역까지 가는 최단 거리

max_item = 0
for i in range (1, n+1):
  # i번째 지역에 떨어졌을 때 j까지 거리가 m 이하라면 아이템 수집 가능
  cur_item = 0
  for j in range (1, n+1):
    if dp[i][j] <= m:
      cur_item += items[j]
  max_item = max(max_item, cur_item)

print(max_item)