import sys
import heapq
input = sys.stdin.readline

n = int(input())
h = []
for _ in range (n):
  x = int(input())

  if x == 0:
    if h:
      print(-heapq.heappop(h))
    else:
      print(0)
  else:
    heapq.heappush(h, -x) # 가장 작은 수부터 출력하므로 부호를 반대로 해야 최대값부터 출력 가능