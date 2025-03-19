import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

n, m = map(int, input().split())
graph = [[] for _ in range (n+1)] # cost between nodes
cost = [INF] * (n+1)

for _ in range (m):
  a, b, c = map(int, input().split())
  graph[a].append((c, b)) # cost, node
  graph[b].append((c, a))

def dijkstra(s):
  heap = []
  cost[s] = 0 # initialize the cost of oneself to zero
  heapq.heappush(heap, (0, s)) # append (cost, node) into heap

  while heap:
    cc, cn = heapq.heappop(heap) # current cost, current node
    if cost[cn] < cc: # no need to calculate if current cost is more expensive than cost of current node
      continue

    for nc, nn in graph[cn]: # check next cost and next node of current node
      tc = cc + nc # total cost is sum of current cost and next cost

      if tc < cost[nn]: # if total cost is smaller than cost of next node, renew the cost of next node
        cost[nn] = tc
        heapq.heappush(heap, (tc, nn)) # append new minimum into heap
  
  return cost[n]

print(dijkstra(1))