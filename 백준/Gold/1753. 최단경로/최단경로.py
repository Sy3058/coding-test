import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
k = int(input())

dp = [INF] * (V+1) # 가중치 테이블
heap = []
graph = [[] for _ in range (V+1)]

for _ in range (E):
  u, v, w = map(int, input().split())
  graph[u].append((w, v)) # (가중치, 목적지 노드)

def dijkstra(s):
  dp[s] = 0 # 시작 정점의 가중치는 0
  heapq.heappush(heap, (0, s))

  while heap:
    weight, cur = heapq.heappop(heap) # 가중치, 현재 노드

    if dp[cur] < weight: # 더 가중치가 크면 무시
      continue

    for w, nn in graph[cur]: # next node
      nw = w + weight # 다음 노드의 가중치는 현재 가중치 + 다음 가중치
      if nw < dp[nn]:
        dp[nn] = nw # 가중치 테이블 업데이트
        heapq.heappush(heap, (nw, nn))

dijkstra(k)

for i in range (1, V+1):
  if dp[i] == INF:
    print("INF")
  else:
    print(dp[i])
