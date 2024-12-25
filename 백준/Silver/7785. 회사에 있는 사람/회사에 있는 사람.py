import sys

n = int(sys.stdin.readline())
company = set()
for _ in range (n):
  name, record = sys.stdin.readline().strip().split()
  if record == 'enter':
    company.add(name) # enter이면 명단에 추가
  else:
    company.discard(name) # leave인 경우 명단에서 제거

ans = list(company)
ans.sort(reverse = True) # 사전 역순

for name in ans:
  print(name)