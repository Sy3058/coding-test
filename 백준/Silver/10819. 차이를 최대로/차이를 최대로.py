import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
visited = [False] * n
mv = 0

def calc(arr):
  hap = 0
  for i in range (n - 1):
    hap += abs(arr[i] - arr[i+1])
  
  return hap

def sol(narr):
  global mv
  if len(narr) == n:
    mv = max(calc(narr), mv)
    return
  
  for i in range (n):
    if not visited[i]:
      narr.append(arr[i])
      visited[i] = True
      sol(narr)
      narr.pop()
      visited[i] = False

sol([])
print(mv)