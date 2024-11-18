import sys

N, M = map(int, sys.stdin.readline().split())
buckets = [i for i in range (1, N+1)]

for _ in range (M):
  i, j = map(int, sys.stdin.readline().split())
  i -= 1; j-=1 # 인덱스이므로 1씩 줄여줘야함

  tmp = buckets[i:j+1]
  tmp = tmp[::-1]
  buckets[i:j+1] = tmp

print(' '.join(map(str, buckets)))