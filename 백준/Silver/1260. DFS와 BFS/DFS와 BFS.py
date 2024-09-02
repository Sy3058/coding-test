import sys

N, M, V = map(int, sys.stdin.readline().split())

# 행렬 만들기
graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range (M):
  a, b = map(int, sys.stdin.readline().split())
  graph[a][b] = graph[b][a] = 1 # 정점 간의 연결을 표시

# 방문 리스트 행렬 (정점의 수만큼 방문 리스트 생성)
visitedD = [0]*(N+1) # dfs에서 사용할 방문 리스트
visitedB = visitedD.copy() # bfs에서 사용할 방문 리스트

# DFS : 깊이 우선 탐색
def dfs(V):
  answer = []
  visitedD[V] = 1 # 탐색된 정점의 번호 방문 처리
  print(V, end = ' ') # 탐색 순서대로 번호 호출
  for i in range (1, N+1):
    if graph[V][i] == 1 and visitedD[i] == 0: # V와 연결된 정점 중 스택에 들어간 적 없는 정점
      dfs(i) # 재귀 호출을 통해 그 다음으로 연결된 정점 탐색
  
# BFS : 너비 우선 탐색
def bfs(V):
  queue = [V]
  visitedB[V] = 1 # 탐색을 시작할 정점의 번호 방문 처리
  while queue: # 큐에 정점이 존재하는 동안 계속 실행
    V = queue.pop(0) # queue의 0번째 요소 제거 (방문한 정점 제거)
    print(V, end = ' ') # 탐색 순서대로 번호 호출
    for i in range(1, N+1):
      if (graph[V][i] == 1 and visitedB[i] == 0): # V와 연결된 정점 중 큐에 들어간 적 없는 정점
        queue.append(i) # 연결 된 모든 노드를 queue에 추가
        visitedB[i] = 1 # queue에 넣은 정점 방문 처리

dfs(V)
print()
bfs(V)
