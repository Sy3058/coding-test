def find(x):
  if x != parent[x]:
    parent[x] = find(parent[x])
  return parent[x]

def union(a, b):
  rootA = find(a)
  rootB = find(b)
  if rootA != rootB:
    parent[rootB] = rootA
    return True
  return False

n = int(input())
parent = [i for i in range(n)] # 0부터 n-1까지 인덱스를 사용
edges = []
nodes = []

for i in range(n):
    x, y, z = map(int, input().split())
    nodes.append((x, y, z, i)) # 행성 좌표와 원래 인덱스를 함께 저장

# x 좌표를 기준으로 정렬하고 간선 추가
nodes.sort(key=lambda p: p[0])
for i in range(n - 1):
    dist = abs(nodes[i][0] - nodes[i+1][0])
    # edge에 거리와 노드 저장
    edges.append((dist, nodes[i][3], nodes[i+1][3]))

# y 좌표를 기준으로 정렬하고 간선 추가
nodes.sort(key=lambda p: p[1])
for i in range(n - 1):
    dist = abs(nodes[i][1] - nodes[i+1][1])
    edges.append((dist, nodes[i][3], nodes[i+1][3]))

# z 좌표를 기준으로 정렬하고 간선 추가
nodes.sort(key=lambda p: p[2])
for i in range(n - 1):
    dist = abs(nodes[i][2] - nodes[i+1][2])
    edges.append((dist, nodes[i][3], nodes[i+1][3]))

edges.sort()
total_cost = 0
mst_edges = 0

# 크루스칼 알고리즘
for dist, u, v in edges:
    if union(u, v):
        total_cost += dist
        mst_edges += 1
        if mst_edges == n - 1:
            break

print(total_cost)