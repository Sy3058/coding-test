import sys
input = sys.stdin.readline

h, w = map(int, input().split())
height = list(map(int, input().split()))

wall = {i:[] for i in range (h)}
water = 0

for i in range (w):
  for j in range (height[i]):
    wall[j].append(i)

for i in range (h):
  col = wall[i]
  for j in range (1, len(col)):
    water += col[j] - col[j-1] - 1

print(water)