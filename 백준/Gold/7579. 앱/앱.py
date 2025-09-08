n, m = map(int, input().split()) # m바이트의 메모리까지
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

total_cost = sum(costs)

# dp[j]는 총 코스트가 j일 때 확보할 수 있는 최대 메모리
# 초기값은 모두 0
dp = [0] * (total_cost + 1)

# 각 앱을 순회하며 dp 테이블 갱신
for i in range (n):
  me = memories[i]
  c = costs[i]

  # 뒤에서부터 순회하며 중복 방지
  for j in range (total_cost, c - 1, -1):
    # 현재 앱을 비활성화하는 경우, 활성화하는 경우 중 더 큰 메모리 선택
    dp[j] = max(dp[j], dp[j - c] + me)

# 최소 메모리 M을 만족하는 가장 작은 코스트 찾기
for j in range (total_cost + 1):
  if dp[j] >= m:
    print(j)
    break