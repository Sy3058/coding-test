import sys
import math
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())
ans = 0

for i in range (n):
  if arr[i] <= b:
    ans += 1
  else:
    proctor = math.ceil((arr[i] - b) / c) + 1
    ans += proctor

print(ans)