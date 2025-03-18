import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
cnt = 0
good = []

arr.sort()

for i in range (n):
  l = 0
  r = n-1
  while l < r:
    if l == i: # 자기 자신은 포함할 수 없음
      l += 1
      continue
    if r == i:
      r -= 1
      continue
    
    hap = arr[l] + arr[r]
    if hap == arr[i]:
      cnt += 1
      break

    if hap > arr[i]:
      r -= 1
    else:
      l += 1

print(cnt)