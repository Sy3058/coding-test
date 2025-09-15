import heapq

n = int(input())
m = int(input())
INF = float('inf')

# 그래프 정보 저장
graph = [[] for _ in range (n + 1)]

dist = [INF] * (n + 1) # 최단 거리를 저장
for _ in range (m):
  s, e, c = map(int, input().split())
  graph[s].append((e, c))

start, end = map(int, input().split())

# (거리, 노드) 형태로 우선순위 큐에 저장
hp = []
heapq.heappush(hp, (0, start))
dist[start] = 0

while hp:
  # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
  d, now = heapq.heappop(hp)

  # 현재 노드가 이미 처리된 적이 있다면 무시
  if dist[now] < d:
    continue

  # 현재 노드와 연결된 인접 노드들 확인
  for i in graph[now]:
    c = d + i[1]

    # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
    if c < dist[i[0]]:
      dist[i[0]] = c
      heapq.heappush(hp, (c, i[0]))

print(dist[end])