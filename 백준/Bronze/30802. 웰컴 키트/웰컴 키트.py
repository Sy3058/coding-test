import sys
import math
input = sys.stdin.readline

n = int(input())
tshirt = list(map(int, input().split()))
t, p = map(int, input().split())

ts = 0
for i in range (6):
    ts += math.ceil(tshirt[i] / t)
print(ts)
print(n//p, n%p)