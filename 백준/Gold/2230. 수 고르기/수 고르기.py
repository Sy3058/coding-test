import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(int(input()) for _ in range (n))
arr.sort()

def solution(arr, n, m):
  l, r = 0, 0
  mv = float('inf') # min value
  while r < n:
    if arr[r] - arr[l] == m:
      return m
    
    if arr[r] - arr[l] < m: # 큰 수가 더 커져야 차가 커짐
      r += 1
    
    else: # 작은 수가 더 커져야 차가 줄어듦
      mv = min(mv, arr[r] - arr[l])
      l += 1

  return mv

print(solution(arr, n, m))