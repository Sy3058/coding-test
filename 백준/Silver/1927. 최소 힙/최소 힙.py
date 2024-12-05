import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for _ in range (n):
  x = int(sys.stdin.readline())

  if not heap and x == 0:
    print(0)
  
  elif x == 0:
    print(heapq.heappop(heap))
  
  else:
    heapq.heappush(heap, x)