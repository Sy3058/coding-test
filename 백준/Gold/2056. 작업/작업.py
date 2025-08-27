import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = {i:set() for i in range (1, n+1)}
in_degree = [0] * (n+1)
work_time = [0] * (n+1)
dp = [0] * (n+1)

for i in range (1, n+1): # 작업번호는 1부터 시작
  time, cnt, *li = list(map(int, input().split())) # 걸리는 시간, 선행 관계에 있는 적압덜의 개수, *선행 관계에 있는 작업들
  work_time[i] = time
  for j in range (cnt):
    graph[li[j]].add(i) # i와 li[j]를 연결
    in_degree[i] += 1 # li[j]의 진입 차수 증가

def topology_sort():
  result = []
  nv = deque()
  
  # 진입차수가 0인 노드를 큐에 삽입
  for i in range (1, n+1):
    if in_degree[i] == 0:
      nv.append(i)
      dp[i] = work_time[i] # 바로 시작 가능한 작업은 시간 그대로 초기화
  
  # 큐가 완전히 빌 때까지 진입차수가 0인 노드를 큐에 삽입
  while nv:
    cur = nv.popleft()
    result.append(cur)

    # 해당 원소와 연결된 노드들의 진입 차수 -1
    for nxt in graph[cur]:
      in_degree[nxt] -= 1
      dp[nxt] = max(dp[nxt], dp[cur] + work_time[nxt]) # 선행 작업 중 가장 오래 걸리는 것이 끝난 후에 작업을 진행해야 함
      # 이때 진입 차수가 0이 됐다면 큐에 삽입
      if in_degree[nxt] == 0:
        nv.append(nxt)
  
  print(max(dp))

topology_sort()