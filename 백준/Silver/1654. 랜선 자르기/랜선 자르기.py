import sys
input = sys.stdin.readline

k, n = map(int, input().split())
l = [int(input()) for _ in range (k)]

high = max(l)
low = 1

while low <= high:
  cnt = 0
  mid = (low + high) // 2
  for i in range (k):
    cnt += l[i] // mid
  
  if cnt >= n:
    low = mid + 1
  else:
    high = mid - 1

print(high)