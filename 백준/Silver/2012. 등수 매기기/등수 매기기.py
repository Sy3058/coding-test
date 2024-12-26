import sys

n = int(sys.stdin.readline())
erank = [int(sys.stdin.readline()) for _ in range (n)]

erank.sort()
for i in range (n):
  erank[i] = abs(erank[i] - (i+1))

print(sum(erank))