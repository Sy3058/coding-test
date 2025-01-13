import sys
input = sys.stdin.readline

n, k = map(int, input().split())
hp = list(input().strip())
hpb = [False for _ in range (n)]

for i in range (n):
  if hp[i] == 'P':
    hpb[i] = 'P'

cnt = 0

for i in range (n):
  if hp[i] == 'P':
    for j in range (-k, k+1):
      if 0 <= i+j < n and not hpb[i+j]:
        hpb[i+j] = True
        cnt += 1
        break

print(cnt)