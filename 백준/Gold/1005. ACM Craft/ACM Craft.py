import sys
from collections import deque
input = sys.stdin.readline

for tc in range (int(input())):
  n, k = map(int, input().split())
  b_time = [0] + list(map(int, input().split()))
  in_degree = [0 for _ in range (n + 1)]
  graph = {i:[] for i in range (1, n+1)}
  for _ in range (k):
    x, y = map(int, input().split()) # X 짓고 Y 짓기
    in_degree[y] += 1
    graph[x].append(y)
  w = int(input()) # 건설해야 할 건물의 번호
  dp = [0 for _ in range (n + 1)]

  can_build = deque()
  for i in range (1, n+1):
    if in_degree[i] == 0: # 진입 차수가 없는 것만 건설 가능
      can_build.append(i)
      dp[i] = b_time[i]
  
  while can_build:
    cur = can_build.popleft()

    for i in graph[cur]:
      in_degree[i] -= 1
      dp[i] = max(dp[i], dp[cur] + b_time[i])
      if in_degree[i] == 0:
        can_build.append(i)

  print(dp[w])
  