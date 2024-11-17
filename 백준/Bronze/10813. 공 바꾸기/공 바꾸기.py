import sys

N, M = map(int, sys.stdin.readline().split())
arr = [i+1 for i in range (N)]

for _ in range (M):
  i, j = map(int, sys.stdin.readline().split())
  if i == j:
    continue

  i -= 1; j -= 1
  tmp = arr[i]
  arr[i] = arr[j]
  arr[j] = tmp

print(' '.join(map(str, arr)))