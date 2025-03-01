import sys
input = sys.stdin.readline

n = int(input())
xy = [tuple(map(int, input().split())) for _ in range (n)]

for x, y in xy:
  rank = 1
  for p, q in xy:
    if x < p and y < q: # 키와 몸무게 중 하나라도 작으면 등수 + 1
      rank += 1
  print(rank, end = ' ')