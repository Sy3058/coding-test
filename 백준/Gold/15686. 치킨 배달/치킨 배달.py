import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range (n)]

house = []
chicken = []

for i in range (n):
  for j in range (n):
    if city[i][j] == 1:
      house.append((i, j))
    elif city[i][j] == 2:
      chicken.append((i, j))

def get_chicken_distance(house, chicken):
  td = 0 # total distance
  for h in house:
    cd = float('inf') # minimum chicken distance
    for c in chicken:
      x1, y1 = h
      x2, y2 = c
      cd = min(cd, abs(x1-x2) + abs(y1-y2)) # update minimum chicken distance
    td += cd # add chicken distance to total distance
  return td

pc = list(combinations(chicken, m)) # generate a list of combinations of m items selected from chicken shops

ans = float('inf')
for cs in pc:
  tcd = get_chicken_distance(house, cs) # total chicken distance
  ans = min(tcd, ans) # update minimum total chicken distance

print(ans)