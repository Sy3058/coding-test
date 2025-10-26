import sys
input = sys.stdin.readline

n = int(input())
rods = [int(input()) for _ in range (n)]
base = rods[-1]
cnt = 1
for i in range (n-2, -1, -1):
  if rods[i] > base:
    base = rods[i]
    cnt += 1
print(cnt)