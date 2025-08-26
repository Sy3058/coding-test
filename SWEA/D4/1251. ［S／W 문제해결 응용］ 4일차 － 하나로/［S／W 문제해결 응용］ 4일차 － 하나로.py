def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x]) # 경로 압축
  return parent[x]

def union(a, b):
  rootA = find(a)
  rootB = find(b)

  if rootA != rootB:
    parent[rootB] = rootA
    return True # union 가능
  return False # union 불가능

for tc in range (1, int(input()) + 1):
  n = int(input())
  xs = list(map(int, input().split())) # x 좌표
  ys = list(map(int, input().split())) # y 좌표
  e = float(input()) # 부담 세율 (실수)

  # 간선 (a, b)를 연결한 비용으로 맵 생성
  # 노드 번호 기준 부모 테이블 생성
  parent = [i for i in range (n+1)]
  edges = [] # 간선 정보를 담을 리스트

  for i in range (n):
    for j in range (i+1, n):
      dist = (xs[i]-xs[j])**2 + (ys[i]-ys[j])**2 # 간선 두개 사이의 거리
      cost = e * dist
      edges.append((cost, i, j)) # i번째 edge와 j번째 edge 사이의 환경부담금 cost
  
  edges.sort(key = lambda x:x[0]) # cost 기준 오름차순 정렬

  total_cost = 0 # 최소 환경 부담금
  cnt = 0 # 간선의 개수 (n-1개여야함)

  for cost, a, b in edges:
    if union(a, b): # a와 b를 합칠 수 있다면 (사이클을 형성하지 않는다면)
      total_cost += cost
      cnt += 1
      if cnt == n-1:
        break
  
  print(f"#{tc} {round(total_cost)}") # 최소 환경 부담금은 소수 첫째 자리에서 반올림