import sys

N = int(sys.stdin.readline())
Ps = list(map(int, sys.stdin.readline().split()))

# 합의 최솟값이므로 최솟값부터 순서대로 더해져야함

Ps.sort()
hap = 0

for i in range (len(Ps)):
  hap += Ps[i] * N
  N -= 1

print(hap)