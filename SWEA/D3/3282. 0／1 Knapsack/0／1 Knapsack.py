# knapsack 알고리즘
for tc in range (1, int(input()) + 1):
  n, k = map(int, input().split())
  # dp계산을 편하게 하기 위해 앞에 더미 데이터 추가
  items = [[0, 0]] + [list(map(int, input().split())) for _ in range (n)]

  # dp[i][j] = 부피 j만큼 가방에 담을 수 있을 때 i개의 물건 중 담을 수 있는 최대 가치
  dp = [[0] * (k + 1) for _ in range (n+1)]

  for i in range (1, n+1): # 가지고 있는 물건을 순회하며 확인
    for j in range (1, k+1): # 부피 제한이 j
      v = items[i][0]
      c = items[i][1]

      if j < v:
        # 현재 물건의 부피가 검사하는 부피보다 작으면 넣을 수 없음
        dp[i][j] = dp[i-1][j]
      
      else:
        # 현재 물건을 넣지 않는 것과 넣는 것 중 가치가 더 높을 것을 저장
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-v] + c)
  
  print(f"#{tc} {dp[n][k]}")