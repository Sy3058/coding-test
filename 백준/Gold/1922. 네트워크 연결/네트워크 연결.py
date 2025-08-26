import sys
input = sys.stdin.readline

def find(x):
  if (x != parent[x]):
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
m = int(input())
parent = [i for i in range (n+1)]
edges = [] # 간선들을 넣을 리스트 (c, a, b) 형태로 저장
for _ in range (m):
  a, b, c = map(int, input().split()) # a 컴퓨터와 b 컴퓨터를 연결하는 비용 c
  edges.append((c, a, b))

edges.sort(key = lambda x : x[0]) # cost 기준 정렬

total_cost = 0
cnt = 0

for e in edges:
  c, a, b = e
  if union(a, b): # 합칠 수 있는 경우 사이클을 형성하지 않는 것
    total_cost += c
    cnt += 1
    if cnt == n - 1: # 간선의 개수는 n-1개까지 존재
      break

print(total_cost)