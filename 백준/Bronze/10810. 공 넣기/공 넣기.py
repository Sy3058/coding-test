import sys

N, M = map(int, sys.stdin.readline().split())
arr = [0] * N

for _ in range (M):
  i, j, k = map(int, sys.stdin.readline().split())  
  i-=1; j-=1 # 바구니의 인덱스이므로 -1
  for num in range (i, j+1):
    arr[num] = k

print(' '.join(map(str, arr)))