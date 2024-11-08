import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
i = 0 # left pointer
j = 0 # right pointer
cnt = 0

while j < N:
  tmp = sum(arr[i:j+1])

  if tmp == M:
    cnt += 1
    i += 1
    j += 1
  
  elif tmp < M: # 합을 늘려야하므로 j를 늘려야 함
    j += 1
  
  else: # 합을 줄여야하므로 i를 늘려야 함
    i += 1

print(cnt)