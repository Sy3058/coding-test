import sys

n, ns, p = map(int, sys.stdin.readline().split())
if n == 0:
  print(1)
else:
  rank = list(map(int, sys.stdin.readline().split()))
  if n == p and rank[-1] >= ns: # n이 p보다 작으면 랭킹에 무조건 들 수 있으므로 n == p 조건 필요
    print(-1)
  
  else:
    r = n+1
    for i in range (n):
      if rank[i] <= ns:
        r = i + 1
        break
    
    print(r)