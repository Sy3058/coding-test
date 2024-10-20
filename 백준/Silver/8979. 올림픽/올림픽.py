N, K = map(int, input().split()) # 국가의 수, 등수를 알고 싶은 국가
medals = {}

for _ in range (N):
  c, g, s, b = map(int, input().split()) # country, gold, silver, bronze
  medals[c] = (g, s, b)

rank = sorted(medals.items(), key = lambda x: (x[1][0], x[1][1], x[1][2]), reverse = True) # g, s, b가 큰 순으로 정렬

ranking = 1
tmp = 1 # 메달 수가 동일한 국가의 수
for i in range (1, N):
  if rank[i][1] == rank[i-1][1]: # 앞의 국가와 메달이 동일할 때
    tmp += 1
  else: # 다를 때
    ranking += tmp
    tmp = 1 # 메달 수가 동일한 국가의 수 초기화
  if rank[i][0] == K:
    break

print(ranking)