import sys

n, m = map(int, sys.stdin.readline().split())
mons_idx = {} # key = idx, value = name

for i in range (n):
  mon = sys.stdin.readline().strip()
  mons_idx[i+1] = mon

mons_name = {value:key for key, value in mons_idx.items()} # key = name, value = idx

for _ in range (m):
  ans = sys.stdin.readline().strip()
  if ans.isalpha():
    print(mons_name[ans])
  else:
    ans = int(ans)
    print(mons_idx[ans])