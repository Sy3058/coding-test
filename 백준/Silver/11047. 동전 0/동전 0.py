import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range (n)]
coin.reverse()
cnt = 0

for i in range (n):
  cnt += k//coin[i]
  k = k%coin[i]
  if k == 0:
    break

print(cnt)