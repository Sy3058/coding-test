import sys

n, m = map(int, sys.stdin.readline().split())
li = set([sys.stdin.readline().strip() for _ in range (n)])
se = set([sys.stdin.readline().strip() for _ in range (m)])

lise = li & se
ans = list(lise)
ans.sort()

print(len(ans))
for name in ans:
  print(name)