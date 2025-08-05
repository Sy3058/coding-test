import sys
input = sys.stdin.readline

s, p = map(int, input().split())
dna = list(input().strip())
reqnum = list(map(int, input().split()))
req = {'A':reqnum[0], 'C':reqnum[1], 'G':reqnum[2], 'T':reqnum[3]}
cnt = 0

# 기본 세팅 - 0부터 p-1까지 dna 개수를 req에서 삭제
for i in range (p):
  req[dna[i]] -= 1

if max(req.values()) <= 0:
  cnt += 1

for i in range (p, s):
  req[dna[i]] -= 1 # 사용된 요소
  req[dna[i-p]] += 1 # 반환된 요소
  # req의 value가 1 이상이면 사용되어야하나 사용되지 않은 것
  if max(req.values()) <= 0:
    cnt += 1

print(cnt)