import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range (n)]
visited = [[0] * n for _ in range (n)]
gd = {i:[] for i in range (n)}

for i in range (n):
  for j in range (n):
    if graph[i][j] == 1:
      gd[i].append(j) # i와 연결된 j를 graph_dictionary에 저장

def dfs(s):
  nv = [s]

  while nv:
    x = nv.pop()

    for y in gd[x]: # i와 연결된 j들을 각각 탐색
      if not visited[s][y]: # s에서 시작했으므로 visited[s][]를 이용해서 갈 수 있는지 확인
        visited[s][y] = 1
        nv.append(y)

for i in range (n): # i부터 n-1까지 확인
  dfs(i)

for i in range (n):
  print(*visited[i])