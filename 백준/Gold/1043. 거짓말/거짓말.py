def dfs(cur): # 진실을 아는 cur와 연결된 모든 사람 찾기
  know[cur] = True

  for nxt in range (1, n+1): # 사람 번호는 1부터 시작
    if graph[cur][nxt] and not know[nxt]: # 같이 파티에 간 적 있는데 진실을 모른다면
      dfs(nxt) # 이 사람을 기준으로 다시 dfs

n, m = map(int, input().split()) # 사람의 수, 파티의 수
tn, *tnum = map(int, input().split()) # 진실을 아는 사람의 수와 번호
graph = [[False] * (n + 1) for _ in range (n + 1)] # i번째 사람과 j번째 사람이 같은 파티에 간 적 있는 지
parties = []

for _ in range (m):
  pn, *pnum = map(int, input().split()) # 파티에 오는 사람의 수와 번호
  parties.append(set(pnum))
  for i in range (pn - 1):
    for j in range (i + 1, pn):
      graph[pnum[i]][pnum[j]] = True
      graph[pnum[j]][pnum[i]] = True

know = [False for _ in range (n + 1)] # 진실을 알고 있는지 확인
for t in tnum:
  dfs(t)

cnt = 0 
for pnum in parties:
  flag = False # 진실만 말해야하는지
  for p in pnum:
    if know[p]: # 진실을 알고있다면
      flag = True # 진실만 말해야함
      break
  
  if not flag:
    cnt += 1

print(cnt)