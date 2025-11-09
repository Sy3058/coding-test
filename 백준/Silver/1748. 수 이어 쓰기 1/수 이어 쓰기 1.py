import sys
import math
input = sys.stdin.readline

# 1 ~ 9까지는 1개(log10), 10 ~ 99까지는 2개(log100) ... 개씩 자릿수가 늘어남
n = int(input())
tmp = int(math.log10(n)) + 1

ans = 0
for i in range (1, tmp):
  ans += 9 * (10 ** (i-1)) * i # 자릿수마다 9 * (10 ** 자릿수) 개씩 늘어남
# 마지막 자리수에선 아래에 해당하는 수만큼 추가됨
ans += (n - 10 ** (tmp - 1) + 1) * tmp
print(ans)