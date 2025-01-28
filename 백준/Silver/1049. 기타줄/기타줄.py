import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p, e = float('inf'), float('inf')
for _ in range (m):
  package, each = map(int, input().split())
  # 돈의 수가 최소이므로 가장 작은 값만 알면 됨
  p = min(p, package)
  e = min(e, each)

np = n//6 # 패키지로 구매
ne = n%6 # 개별 구매

if e*6 <= p: # 패키지보다 개별 구매가 싼 경우
  print(n*e)
else:
  if e*ne >= p: # 개별로 구매해야하는 수량보다 패키지가 싼 경우
    print(p*(np+1))
  else: # 패키지는 패키지대로, 개별 구매는 개별 구매대로 하는 경우
    print(p*np + e*ne)