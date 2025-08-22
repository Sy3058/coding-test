import sys
input = sys.stdin.readline

"""
A -> B -> C와 같이 그래프로 저장하고 위상정렬
"""
from collections import deque

def is_empty():
  for i in range (1, n+1):
    if in_degree[i] != 0: # 모든 진입 차수가 0일 때 종료
      return False
  return True

def topology_sort():
  result = []
  nv = deque()

  # 진입차수가 0인 노드를 큐에 삽입
  for i in range (1, n+1):
    if in_degree[i] == 0:
      nv.append(i)

  # 큐가 빌 때까지 진행
  while nv:
    cur = nv.popleft()
    result.append(cur)

    # 해당 원소와 연결된 노드들의 진입 차수 -1
    for nxt in graph[cur]:
      in_degree[nxt] -= 1
      # 만약 진입 차수가 0이 됐다면 큐에 삽입
      if in_degree[nxt] == 0:
        nv.append(nxt)
  print(*result)

n, m = map(int, input().split())
graph = {i:set() for i in range (1, n+1)}
in_degree = [0] * (n + 1) # 진입 차수
visited = [False] * (n + 1) # 방문 확인
for i in range (m):
  a, b = map(int, input().split())
  graph[a].add(b)
  in_degree[b] += 1

topology_sort()