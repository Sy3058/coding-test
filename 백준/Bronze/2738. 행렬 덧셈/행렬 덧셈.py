import sys

N, M = map(int, sys.stdin.readline().split())
arrn = []
arrm = []
arr = [[0]*M for _ in range (N)]

for _ in range (N):
  row = list(map(int, sys.stdin.readline().split()))
  arrn.append(row)

for _ in range (N):
  row = list(map(int, sys.stdin.readline().split()))
  arrm.append(row)

for i in range (N):
  for j in range (M):
    arr[i][j] = arrn[i][j] + arrm[i][j]
  print(' '.join(map(str, arr[i])))