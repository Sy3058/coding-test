import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
tree = {i:[] for i in range (1, n+1)}

for _ in range (m):
  a, b = map(int, input().split())
  tree[a].append(b)
  tree[b].append(a)

flist = set()
f1l = tree[1] # 상근이의 친구
for f1 in f1l:
  flist.add(f1)
  f2l = tree[f1]
  for f2 in f2l:
    flist.add(f2)

if 1 in flist:
  print(len(flist)-1)
else:
  print(len(flist))