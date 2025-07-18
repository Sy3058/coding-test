import sys
import math
input = sys.stdin.readline

n = int(input())
if n == 0:
    print(0)
    exit()
rates = [int(input()) for _ in range (n)]
rates.sort()
out = math.floor(n * 0.15 + 0.5) # 절사평균 할 명수
print(math.floor(sum(rates[out:n-out]) / (n - 2 * out) + 0.5))