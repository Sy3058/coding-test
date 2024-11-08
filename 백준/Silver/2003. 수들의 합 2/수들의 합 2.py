import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
i = 0 # left pointer
j = 0 # right pointer
cnt = 0
hap = arr[0] # i == 0, j == 0 일 때의 합

while j < N:
  if hap == M:
    cnt += 1
    i += 1
    j += 1
    if j == N:
      break
    hap -= arr[i-1]
    hap += arr[j]
  
  elif hap < M: # 합을 늘려야하므로 j를 늘려야 함
    j += 1
    if j == N:
      break
    hap += arr[j]
  
  else: # 합을 줄여야하므로 i를 늘려야 함
    i += 1
    hap -= arr[i-1]

print(cnt)