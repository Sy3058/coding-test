import sys
import math

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
x_li = tuple(map(int, sys.stdin.readline().split()))

mlen = 0
left = x_li[0] - 0
right = n - x_li[-1]

side = max(left, right)

for i in range (1, m):
  mlen = max(mlen, x_li[i] - x_li[i-1])

ans = math.ceil(mlen/2)

print(max(ans, side))