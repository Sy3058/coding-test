import sys
input = sys.stdin.readline
from collections import deque

# 모든 진입차수가 0이 되면 종료하기 위한 조건
def is_empty():
  for i in range (1, n+1):
    if in_degree[i] != 0:
      return False
    return True

def topology_sort():
  result = []
  nv = deque() # 진입차수가 0인 노드

  for i in range (1, n+1):
    if in_degree[i] == 0:
      nv.append(i)
  
  # 큐가 빌 때까지 진입차수가 0인 노드 찾기
  while nv:
    cur = nv.popleft() # FIFO 필요
    result.append(cur)

    # 해당 원소와 연결된 노드들의 진입 차수 -1
    for nxt in graph[cur]:
      in_degree[nxt] -= 1
      # 만약 진입차수가 0이 되면 큐에 삽입
      if in_degree[nxt] == 0:
        nv.append(nxt)
  if len(result) != n:
    print(0)
  else:
    for i in result:
      print(i)

n, m = map(int, input().split())
in_degree = [0] * (n+1) # 진입 차수
graph = {i:[] for i in range (1, n+1)}
for _ in range (m):
  num, *order = map(int, input().split())
  for i in range (num - 1):
    graph[order[i]].append(order[i+1])
    in_degree[order[i+1]] += 1

topology_sort()