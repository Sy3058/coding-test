import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
for i in range (1, int(n**0.5) + 1):
  for j in range (i, n // i + 1):
    cnt += 1

print(cnt)