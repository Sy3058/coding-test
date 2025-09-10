for tc in range (1, int(input()) + 1):
  data = list(map(int, input().split()))
  n = data[0]
  graph = []
  for i in range (n):
    # 행 우선으로 주어지므로 n개씩 끊어서 graph에 넣기
    graph.append(data[1 + n * i:1 + n * (i + 1)])
  
  INF = float('inf')
  ans = INF

  for i in range (n):
    for j in range (n):
      if i == j:
        graph[i][j] = INF
        continue
      if graph[i][j] == 0:
        graph[i][j] = INF # 연결되어있지 않으면 무한대로 초기화

  # 플로이드 워셜
  for k in range (n): # 경유지
    for i in range (n): # 출발지점
      if k == i: continue # 경유 출발이 동일하면 확인 안 함
      for j in range (n): # 도착지점
        if i == j or j == k: continue # 셋 중 둘이 동일하면 확인 안 함
        # i에서 j까지의 최단 거리는 i에서 k로 가고 k에서 j로 가는 값의 합과 i에서 바로 j로 가는 값 중 더 작은 값
        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
  
  cc = [0] * n
  for i in range (n):
    for j in range (n):
      if graph[i][j] != INF:
        cc[i] += graph[i][j]

    ans = min(cc[i], ans)
  
  print(f"#{tc} {ans}")
